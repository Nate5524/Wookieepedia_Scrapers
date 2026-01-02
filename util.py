import requests

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
