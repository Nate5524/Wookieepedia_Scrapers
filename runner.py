import json

import fandom
from tqdm import tqdm
from wakepy import keep
from urllib.parse import quote

from util import get_category_members
from config import *

fandom.set_wiki("starwars")


def parse_selected_options():
    for selection in selected_options:
        opt = OPTIONS[selection]
        episodes = []
        skipped = []
        titles = get_category_members(opt["category"])
        maxlen = max([len(t) for t in titles])

        print("Parsing Category:", opt["name"])
        # For each episode, log its details into the episodes array
        bar = tqdm(titles, desc="Fetching episodes")
        for title in bar:
            bar.set_postfix_str(title + " " * (maxlen - len(title)))

            if title is None or type(title) != str:
                continue
            page = fandom.page(title)

            real_title = title
            if len(title) >= 9 and "(episode)" == title[-9:]:
                real_title = title[:-9]
            real_title = real_title.strip()

            description = page.section("Official description")
            if description is None:
                page.section("Publisher's summary")
            if description is None:
                description = ""
            else:
                description = description.split("\n")[1:][0]

            crawl = page.section("Opening crawl")
            if crawl is None:
                crawl = ""
            else:
                crawl = " ".join(crawl.split("\n")[2:])

            infobox_data = None
            try:
                infobox_data = opt["scraper"](title)
            except Exception as e:
                tqdm.write(f"ERROR - {title}: {e}")
                skipped.append(title)
                continue
            season = infobox_data["season"]
            epnum = infobox_data["episode"]
            date = infobox_data["timeline_canon"]
            irl_date = infobox_data["air_date"]

            # Detect failed attempts to parse
            if (
                type(season) != int
                or type(epnum) != str
                or type(date) != str
                or type(irl_date) != str
            ):
                tqdm.write(
                    f"IMPROPER INFO - {title}: {season}:{type(season)}, {epnum}:{type(epnum)}, {date}:{type(date)}, {irl_date}:{type(irl_date)}"
                )
                tqdm.write(
                    f"IMPROPER INFO - {title}: {season}, {epnum}, {date}, {irl_date}"
                )
                skipped.append(title)
                continue

            episodes.append(
                {
                    "title": real_title,
                    "link": "https://"
                    + quote("starwars.fandom.com/wiki/{title.replace(' ', '_')}"),
                    "description": description,
                    "crawl": crawl,
                    "season": season,
                    "episode": epnum,
                    "date": date,
                    "irl_date": irl_date,
                }
            )

        print(f"\n\nSucessfully parsed {len(episodes)} episodes!")
        print(f"Skipped {len(skipped)} episodes:")
        for skip in skipped:
            print(f"   - {skip}")
        # Save episodes array into local JSON
        with open(opt["json"], "w", encoding="utf-8") as f:
            json.dump(episodes, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    if prohibit_sleep:
        with keep.running():
            parse_selected_options()
    else:
        parse_selected_options()
