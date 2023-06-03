import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser

URL = "https://www.basketball-reference.com/leagues/NBA_2023_totals.html"

# Class representing an NBA player, contains all information required for performance analysis
class Player:
    def __init__(self, name, position, games_played, minutes_played, 
                 fg_attempted, fg_percentage, threept_attempted, 
                 threept_percentage, ft_attempted, ft_percentage, 
                 rebounds, assists, steals, blocks, points):
        self.name = name
        self.position = position
        self.games_played = games_played
        self.minutes_played = minutes_played
        self.fg_attempted = fg_attempted
        self.fg_percentage = fg_percentage
        self.threept_attempted = threept_attempted
        self.threept_percentage = threept_percentage
        self.ft_attempted = ft_attempted
        self.ft_percentage = ft_percentage
        self.rebounds = rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.points = points

# Given a url, scrapes all HTML and returns a requests page object
def scrape_site(url):
    page = requests.get(url)
    if page.status_code != 200:
        raise Exception(f"Error grabbing page: {page.status_code}")
    return page


# Given a requests page object, parses and returns a list of player data
def create_player_data_list(page):
    soup = BeautifulSoup(page.text, features="html.parser")
    soup_total_stats = soup.find_all("tr", class_="full_table")
    return soup_total_stats


# Given a list of player data, creates player objects and populates a global data structure
def create_player_objects(player_data_list):
    for player_data in player_data_list:
        soup = BeautifulSoup(str(player_data), features="html.parser")
        print(soup.tr.td.a)  # prints tage with player name

page = scrape_site(URL)
player_data_list = create_player_data_list(page)
create_player_objects(player_data_list)