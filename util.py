import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

API_URL = "https://starwars.fandom.com/api.php"


def get_category_members(category):
    # Get all episodes of the clone wars from the wookieepedia category
    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": category,
        "cmlimit": "max",
    }
    r = requests.get(API_URL, params=params)
    data = r.json()
    return [m["title"] for m in data["query"]["categorymembers"]]


def fetch_episode(title):
    url = "https://" + quote(f"starwars.fandom.com/wiki/{title.replace(' ', '_')}")
    r = requests.get(url)
    if r.status_code != 200:
        print(f"❌ Failed to fetch {title}")
        return {}
    return r.text


def fetch_infobox(title):
    r = fetch_episode(title)
    soup = BeautifulSoup(r, "html.parser")
    infobox = soup.find("aside", class_="portable-infobox")
    if not infobox:
        print(f"⚠️ No infobox found for {title}")
        return {}
    return infobox
