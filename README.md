# Wookieepedia Scrapers
This repo houses a wookieepedia scraper that I made to get some data for a side project of mine. 

*Don't see something you want?* Feel free to reach out and I might get around to it (or if you want it done within any reasonable amount of time, modification to this repo is probably a better option).

## Installation
This project runs in Python3.
For easy installation of dependencies, run ```pip install -r requirements.txt```. Use of a venv is recommended.

## Usage
To run this program, simply run the [`runner.py`](./runner.py) script. All configurations are handled by [`config.py`](./config.py) to control the runner script.

## Supported Content
This is a list of all of the content that the program can parse as of `1/1/2026`.
- The Acolyte
- Ahsoka
- Andor
- The Bad Batch
- The Book of Boba Fett
- The Clone Wars
- The Mandalorian
- Obi-Wan Kenobi
- Rebels
- Resistance
- Skeleton Crew
- Tales of the Empire
- Tales of the Jedi
- Tales of the Underworld

## JSON Format
Here are some descriptions of the JSON format that the scraper will output. To further understand them I recommend poking the actual JSON output files. Optional 

### Episodes:
```json
{
    "title": name of this episode
    "link": the url of this episode's Wookieepedia article
    "description": a short description
    "episode": the episode(s) of the entry (ex. "1" or "2-3")
    "date": the BBY/ABY time of this episode (ex. "12 BBY")
    "irl_date": an iso-formatted date string ("YYYY-MM-DD")
    "crawl?": the crawl of this episode - only exists if a crawl exists
    "season?": the season (integer) - doesn't exist on intentionally single-season shows
}
```

## Licensing
Use of Wookieepedia content falls under [CC BY-SA](https://starwars.fandom.com/wiki/Wookieepedia:Copyrights). None of the parsed content is modified by these scripts except to remove links and clean the formatting.

Use of this code falls under the [GNU GPL](./LICENSE) 🄯.