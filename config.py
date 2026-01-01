from scrapers import parse_episodes

############################################
# Constants
############################################

OPTIONS = {
    "Acolyte": {
        "name": "The Acolyte",
        "category": "Category:Star_Wars:_The_Acolyte_episodes",
        "json": "acolyte_episodes.json",
        "scraper": parse_episodes
    },
    "Ahsoka": {
        "name": "Ahsoka",
        "category": "Category:Star_Wars:_Ahsoka_episodes",
        "json": "ahsoka_episodes.json",
        "scraper": parse_episodes,
    },
    "Andor": {
        "name": "Andor",
        "category": "Category:Star_Wars:_Andor_episodes",
        "json": "andor_episodes.json",
        "scraper": parse_episodes,
    },
    "BadBatch": {
        "name": "Star Wars: The Bad Batch",
        "category": "Category:Star_Wars:_The_Bad_Batch_episodes",
        "json": "bad_batch_episodes.json",
        "scraper": parse_episodes,
    },
    "CloneWars": {
        "name": "Star Wars: The Clone Wars",
        "category": "Category:Star_Wars:_The_Clone_Wars_episodes",
        "json": "clone_wars_episodes.json",
        "scraper": parse_episodes,
    },
    "Mandalorian": {
        "name": "The Mandalorian",
        "category": "Category:Star_Wars:_The_Mandalorian_episodes",
        "json": "mandalorian_episodes.json",
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

selected_options = ["Acolyte"]
prohibit_sleep = True
