import json

import fandom
from tqdm import tqdm
from wakepy import keep

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
            if title is None or type(title) != str:
                continue
            bar.set_postfix_str(title + " " * (maxlen - len(title)))
            try:
                opt["scraper"](title, opt, episodes, skipped)
            except Exception as e:
                tqdm.write(f"ERROR - {title}: {e}")
                skipped.append(title)
    print(f"\n\nSucessfully parsed {len(episodes)} episodes!")
    if len(skipped) > 0: print(f"Skipped {len(skipped)} episodes:")
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
