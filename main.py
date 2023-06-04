import requests
import bs4
from typing import Any

URL = "https://www.basketball-reference.com/leagues/NBA_2023_totals.html"

stat_enumerator_map = {
    0: "name", 1: "pos", 2: "age", 3: "team",
    4: "g", 5: "gs", 6: "mp", 7: "fg", 8: "fga",
    9: "fg%", 10: "3p", 11: "3pa", 12: "3p%",
    13: "2p", 14: "2pa", 15: "2p%", 16: "efg%",
    17: "ft", 18: "fta", 19: "ft%", 20: "orb", 
    21: "drb", 22: "trb", 23: "ast", 24: "stl",
    25: "blk", 26: "tov", 27: "pf", 28: "pts"
}

# Given a url, scrapes all HTML and returns a requests page object
def scrape_site(url: str) -> requests.models.Response:
    page = requests.get(url)
    if page.status_code != 200:
        raise Exception(f"Error grabbing page: {page.status_code}")
    return page

# Given a requests page object, parses and returns a list of player data
def create_player_data_list(page: requests.models.Response) -> bs4.element.ResultSet:
    soup = bs4.BeautifulSoup(page.text, features="html.parser")
    soup_total_stats = soup.find_all("tr", class_="full_table")
    return soup_total_stats

# Given a list of player data, creates a dictionary of player objects
def create_player_objects(player_data_list: bs4.element.ResultSet) -> dict[str, dict[str, Any]]:
    player_dict = dict()
    for player_data in player_data_list:
        soup = bs4.BeautifulSoup(str(player_data), features="html.parser")
        stat_list = soup.tr.find_all("td")
        stats = dict()
        for num, stat in enumerate(stat_list):
            stats[stat_enumerator_map[num]] = stat.text
        player_dict[stats["name"]] = stats
    return player_dict


page = scrape_site(URL)
player_data_list = create_player_data_list(page)
player_dict = create_player_objects(player_data_list)

print(player_dict["Stephen Curry"])
