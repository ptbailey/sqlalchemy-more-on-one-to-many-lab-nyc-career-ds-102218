from models import *
from sqlalchemy import create_engine, func


engine = create_engine('sqlite:///sports.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_teams_for_new_york():
    # here we want to return all teams that are associated with New York City
    return session.query(Teams).join(City).filter(City.state == 'NY').all()

def return_players_for_la_dodgers():
    # here we want to return all players that are associated with the LA dodgers
    return session.query(Player).join(Teams).filter(Teams.name == 'LA Dodgers').all()

def return_sorted_new_york_knicks():
    # here we want to return all the players on the New York Knicks
    # sorted in ascending (small -> big) order by their number
    return session.query(Player).join(Teams).filter(Teams.name == 'NY Knicks').\
        order_by(Player.number.asc()).all()

def return_youngest_basket_ball_player_in_new_york():
    # here we want to sort all the players on New York Knicks by age
    # and return the youngest player
    return session.query(Player).join(Teams).filter(Teams.city == ny).\
        filter(Teams.sport == basketball).filter(Player.age != None).\
        order_by(Player.age.asc()).first()

def return_all_players_in_los_angeles():
    # here we want to return all players that are associated with
    # a sports team in LA
    return session.query(Player).join(Teams).filter(Teams.city == la).all()

def return_tallest_player_in_los_angeles():
    # here we want to return the tallest player associted with
    # a sports team in LA
    tallest_player = session.query(Player,func.max(Player.height)).join(Teams).join(City).filter(City.name=='Los Angeles').all()
    return tallest_player.pop()


def return_team_with_heaviest_players():
    # here we want to return the city with the players that
    # have the heaviest average weight (total weight / total players)
    avg_weights = session.query(Player.team_id,func.avg(Player.weight)).group_by(Player.team_id).all()
    return max(list(map(lambda tup: tup[1],avg_weights)))
