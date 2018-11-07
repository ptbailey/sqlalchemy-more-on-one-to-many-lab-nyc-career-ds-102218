from models import *
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///sports.db')

Session = sessionmaker(bind = engine)
session = Session()

# below we are reading the csv files to create the data we will need to create the players
# pandas returns a DataFrame object from reading the CSV
# we then tell the DataFrame object to turn each row into dictionaries
# by giving to_dict the argument "orient='records'"
# we are telling our DataFrame to make each row a dictionary using the column headers
# as the keys for the key value pairs in each new dictionary
# feel free to uncomment lines 18-21 to see each step of the process in your terminal
# ____ example ______
# la_dodgers0 = pd.read_csv('la_dodgers_baseball.csv')
# la_dodgers1 = pd.read_csv('la_dodgers_baseball.csv').to_dict()
# la_dodgers2 = pd.read_csv('la_dodgers_baseball.csv').to_dict(orient='records')
# import pdb; pdb.set_trace()
# __________________
la_dodgers = pd.read_csv('la_dodgers_baseball.csv').to_dict(orient='records')
la_lakers = pd.read_csv('la_lakers_basketball.csv').to_dict(orient='records')
ny_yankees = pd.read_csv('ny_yankees_baseball.csv').to_dict(orient='records')
ny_knicks = pd.read_csv('ny_knicks_basketball.csv').to_dict(orient='records')

#Istantiate Cities
ny = City(name = 'New York', state = 'NY')
la = City(name = 'Los Angeles', state = 'CA')
cities = [ny,la]

#Istantiate Sports
basketball = Sports(name = 'Basketball')
baseball = Sports(name = 'Baseball')
sports = [basketball,baseball]

#Istantiate Teams
la_dodgers_team = Teams(name = 'LA Dodgers', city = la, sport = baseball)
la_lakers_team = Teams(name = 'LA Lakers', city = la, sport = basketball)
ny_yankees_team = Teams(name = 'NY Yankees', city = ny, sport = baseball)
ny_knicks_team = Teams(name = 'NY Knicks', city = ny, sport = basketball)

#Istantiate Players
def heightconvert(height):
    string = ''.join(char for char in height if char.isalnum())
    feet = int(string[0])
    inches = int(string[1:])
    return feet * 12 + inches

def create_players(team_data, team):
    players_per_team = []
    for x in team_data:
        player = Player(name=x.get('name'),age = x.get('age', None),\
        number=x.get('number', None), height= heightconvert(x['height']), \
        weight=x.get('weight', None), team = team)
        players_per_team.append(player)
    return players_per_team

dodgers_roster = create_players(la_dodgers,la_dodgers_team)
lakers_roster = create_players(la_lakers, la_lakers_team)
yankees_roster = create_players(ny_yankees, ny_yankees_team)
knicks_roster = create_players(ny_knicks, ny_knicks_team)

session.add_all(dodgers_roster)
session.add_all(lakers_roster)
session.add_all(yankees_roster)
session.add_all(knicks_roster)
session.add_all(teams)
session.add_all(sports)
session.add_all(cities)

session.commit()

# now that we have the data for each player
# add and commit the players, teams, sports and cities below
# we will need to probably write at least one function to iterate over our data and create the players
# hint: it may be a good idea to creat the Teams, Cities, and Sports first
