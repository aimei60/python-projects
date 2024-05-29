import requests
from requests import get
from pprint import PrettyPrinter

URL = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"

printer = PrettyPrinter()

def get_scoreboard():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()["scoreboard"]
    else:
        raise Exception("Failed to fetch data from the server")

def get_game_date():
    scoreboard = get_scoreboard()
    game_date = scoreboard['gameDate']
    printer.pprint(game_date)
    
get_game_date()