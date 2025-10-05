import fandom, requests, json
from tqdm import tqdm
from bs4 import BeautifulSoup
from datetime import datetime
from collections import defaultdict
import re


fandom.set_wiki("starwars")
BASE_URL = "https://starwars.fandom.com/api.php"


def get_category_members(category):
    # Get all episodes of the clone wars from the wookieepedia category
    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": category,
        "cmlimit": "max"
    }
    r = requests.get(BASE_URL, params=params)
    data = r.json()
    return [m["title"] for m in data["query"]["categorymembers"]]

def get_infobox_data(title):
    """
    Fetches and parses the Infobox from a Wookieepedia episode page.
    Returns: dict with keys like season, episode, air_date, director, writer, etc.
    """
    url = f"https://starwars.fandom.com/wiki/{title.replace(' ', '_')}"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"❌ Failed to fetch {title}")
        return {}

    soup = BeautifulSoup(r.text, "html.parser")
    infobox = soup.find("aside", class_="portable-infobox")
    if not infobox:
        print(f"⚠️ No infobox found for {title}")
        return {}

    data = defaultdict(lambda:None)
    for pair in infobox.find_all("div", class_="pi-item pi-data pi-item-spacing pi-border-color"):
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
            seasons = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7}
            if value.lower() in seasons:
                value = seasons[value.lower()]
            elif "seven" in value.lower():
                value = 7
            data["season"] = value
        elif "episode" in key and "prior" not in key and "next" not in key:
            data["episode"] = int(value)
        elif "air date" in key:
            fstring = "%B %d , %Y"
            value = value[:re.search(r"\d\d\d\d", value).end()]
            data["air_date"] = datetime.strptime(value, fstring).isoformat()
        elif "director" in key:
            data["director"] = value
        elif "writer" in key:
            data["writer"] = value
        elif "runtime" in key:
            data["runtime"] = value
        elif "timeline" in key and "legends" not in key:
            value = value[:re.search(r"(BBY)|(ABY)", value).end()]
            data["timeline_canon"] = value
        elif "timeline" in key and "legends" in key:
            data["timeline_legends"] = value

    return data


episodes = []
skipped = []
titles = get_category_members("Category:Star_Wars:_The_Clone_Wars_episodes")
maxlen = max([len(t) for t in titles])


# For each episode, log its details into the episodes array
bar = tqdm(titles, desc="Fetching episodes")
for title in bar:
    bar.set_postfix_str(" " * (maxlen - len(title)) + title)
    
    if title is None or type(title)!=str: continue
    page = fandom.page(title)
    
    real_title = title
    if len(title) >= 9 and "(episode)" == title[-9:-1]:
        real_title = title[-9:-1]
    
    description = page.section('Official description')
    if description is None:
        page.section("Publisher's summary")
    if description is None:
        description = ""
    else:
        description = description.split("\n")[1:][0]
    
    crawl = page.section('Opening crawl')
    if crawl is None:
        crawl = ""
    else:
        crawl = " ".join(crawl.split("\n")[2:])
        
    infobox_data = get_infobox_data(title)
    season = infobox_data["season"]
    epnum = infobox_data["episode"]
    date = infobox_data["timeline_canon"]
    irl_date = infobox_data["air_date"]
    if type(season) != int or type(epnum) != int or type(date) != str or type(irl_date) != str:
        print(f"{title}: {season}, {epnum}, {date}, {irl_date}")
        skipped.append(title)
        continue
    
    episodes.append({
        "title": real_title,
        "link": f"https://starwars.fandom.com/wiki/{title.replace(' ', '_')}",
        "description": description,
        "crawl": crawl,
        "season": season,
        "episode": epnum,
        "date": date,
        "irl_date": irl_date,
    })

print(f"Sucessfully parsed {len(episodes)} episodes!")
print(f"Skipped {len(skipped)} episodes:")
for skip in skipped:
    print(f"   - {skip}")
# Save episodes array into local JSON
with open("clone_wars_episodes.json", "w", encoding="utf-8") as f:
    json.dump(episodes, f, ensure_ascii=False, indent=2)
    