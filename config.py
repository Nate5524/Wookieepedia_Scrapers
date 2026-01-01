from scrapers import parse_episodes

############################################
# Constants
############################################

OPTIONS = {
    "Andor": {
        "name": "Andor",
        "category": "Category:Star_Wars:_Andor_episodes",
        "json": "andor_episodes.json",
        "scraper": parse_episodes,
    },
    "CloneWars": {
        "name": "Star Wars: The Clone Wars",
        "category": "Category:Star_Wars:_The_Clone_Wars_episodes",
        "json": "clone_wars_episodes.json",
        "scraper": parse_episodes,
    },
    "Rebels": {
        "name": "Star Wars Rebels",
        "category": "Category:Star_Wars_Rebels_episodes",
        "json": "rebels_episodes.json",
        "scraper": parse_episodes,
    },
}


############################################
# Config Options
############################################

selected_options = ["Andor"]
prohibit_sleep = True
