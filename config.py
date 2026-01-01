from scrapers import get_infobox_data

############################################
# Constants
############################################

OPTIONS = {
    "Andor": {
        "name": "Andor",
        "category": "Category:Star_Wars:_Andor_episodes",
        "json": "andor_episodes.json",
        "scraper": get_infobox_data,
    },
    "CloneWars": {
        "name": "Star Wars: The Clone Wars",
        "category": "Category:Star_Wars:_The_Clone_Wars_episodes",
        "json": "clone_wars_episodes.json",
        "scraper": get_infobox_data,
    },
    "Rebels": {
        "name": "Star Wars Rebels",
        "category": "Category:Star_Wars_Rebels_episodes",
        "json": "rebels_episodes.json",
        "scraper": get_infobox_data,
    },
}


############################################
# Config Options
############################################

selected_options = ["Andor"]
prohibit_sleep = True
