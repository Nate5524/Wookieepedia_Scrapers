from urllib.parse import quote
import fandom
from datetime import datetime
from collections import defaultdict
import re

from tqdm import tqdm
from util import fetch_infobox


fandom.set_wiki("starwars")


def get_infobox_data(title):
    """
    Fetches and parses the Infobox from a Wookieepedia episode page.
    Returns: a dict with the cleaned & parsed information.
    The dict has the following shape:
    {
        "season" : int,
        "episode" : str (2-part episodes are stored as "1-2" on Wookieepedia),
        "air_date" : str (iso format),
        "director" : str,
        "writer" : str,
        "runtime" : str,
        "timeline_canon" : str,
        "timeline_legends" : str
    }
    If any of these aren't found, there will be no placeholder in the dict.
    """
    infobox = fetch_infobox(title)

    data = defaultdict(lambda: None)
    for pair in infobox.find_all(
        "div", class_="pi-item pi-data pi-item-spacing pi-border-color"
    ):
        key_el = pair.find("h3", class_="pi-data-label")
        val_el = pair.find("div", class_="pi-data-value")
        if not key_el or not val_el:
            continue

        key = key_el.get_text(strip=True).lower()
        value = val_el.get_text(" ", strip=True)

        # Clean data
        value = re.sub(r"(\s*\[.*?\]\s*)|(\s*\(.*?\)\s*)", " ", value).strip()

        # Normalize common fields
        if "season" in key:
            seasons = {
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9,
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
            }
            for v, k in enumerate(seasons):
                if k in value.lower():
                    value = v
                    break
            data["season"] = value
        elif "episode" in key and "prior" not in key and "next" not in key:
            data["episode"] = value
        elif "air date" in key:
            dates = re.findall(
                (
                    r"(January|February|March|April|May|June|July|August|September|October|November|December)"
                    r" ([1-9]|[12][0-9]|3[01]) , ([0-9]{4})"
                ),
                value,
            )
            if len(dates) > 0:
                value = " ".join(
                    dates[len(dates) // 2]
                )  # TODO: can this be picking be done intelligently?
                data["air_date"] = (
                    datetime.strptime(value, "%B %d %Y").date().isoformat()
                )
        elif "director" in key:
            data["director"] = value
        elif "writer" in key:
            data["writer"] = value
        elif "runtime" in key:
            data["runtime"] = value
        elif "timeline" in key and "legends" not in key:
            value = value[: re.search(r"(BBY)|(ABY)", value).end()]
            data["timeline_canon"] = value
        elif "timeline" in key and "legends" in key:
            data["timeline_legends"] = value

    return data

def parse_episodes(title, opt, episodes, skipped):
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

    infobox_data = get_infobox_data(title)
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
        return

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