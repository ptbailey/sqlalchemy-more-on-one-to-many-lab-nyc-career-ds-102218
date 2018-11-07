from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# write the Player, City, Sport and Team tables below
class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    number = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)
    age = Column(Integer)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Teams', back_populates = 'roster')

class Sports(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    teams = relationship('Teams', back_populates = 'sport')

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    state = Column(String)
    teams = relationship('Teams', back_populates = 'city')

class Teams(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    city_id = Column(Integer, ForeignKey('city.id'))
    city = relationship('City', back_populates = 'teams' )
    sport_id = Column(Integer, ForeignKey('sports.id'))
    sport = relationship('Sports', back_populates = 'teams')
    roster = relationship(Player, back_populates = 'team')



engine = create_engine('sqlite:///sports.db', echo = True)
Base.metadata.create_all(engine)
