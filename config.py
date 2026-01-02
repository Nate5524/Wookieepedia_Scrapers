from scrapers import parse_episodes

############################################
# Constants
############################################

OPTIONS = {
    "Acolyte": {
        "name": "The Acolyte",
        "category": "Category:Star_Wars:_The_Acolyte_episodes",
        "json": "acolyte_episodes.json",
        "scraper": parse_episodes,
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
    "BobaFett": {
        "name": "The Book of Boba Fett",
        "category": "Category:Star_Wars:_The_Book_of_Boba_Fett_episodes",
        "json": "boba_fett_episodes.json",
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
    "ObiWan": {
        "name": "Obi-Wan Kenobi",
        "category": "Category:Star_Wars:_Obi-Wan_Kenobi_episodes",
        "json": "obi-wan_kenobi_episodes.json",
        "scraper": parse_episodes,
    },
    "Rebels": {
        "name": "Star Wars Rebels",
        "category": "Category:Star_Wars_Rebels_episodes",
        "json": "rebels_episodes.json",
        "scraper": parse_episodes,
    },
    "Resistance": {
        "name": "Star Wars: Resistance",
        "category": "Category:Star_Wars_Resistance_episodes",
        "json": "resistance_episodes.json",
        "scraper": parse_episodes,
    },
    "SkeletonCrew": {
        "name": "Skeleton Crew",
        "category": "Category:Star_Wars:_Skeleton_Crew_episodes",
        "json": "skeleton_crew_episodes.json",
        "scraper": parse_episodes,
    },
    "ToE": {
        "name": "Tales of the Empire",
        "category": "Category:Star_Wars:_Tales_of_the_Empire_episodes",
        "json": "tales_of_the_empire_episodes.json",
        "scraper": parse_episodes,
    },
    "ToJ": {
        "name": "Tales of the Jedi",
        "category": "Category:Star_Wars:_Tales_of_the_Jedi_episodes",
        "json": "tales_of_the_jedi_episodes.json",
        "scraper": parse_episodes,
    },
    "ToU": {
        "name": "Tales of the Underworld",
        "category": "Category:Star_Wars:_Tales_of_the_Underworld_episodes",
        "json": "tales_of_the_underworld_episodes.json",
        "scraper": parse_episodes,
    },
}


############################################
# Config Options
############################################

selected_options = OPTIONS.keys()
prohibit_sleep = True
