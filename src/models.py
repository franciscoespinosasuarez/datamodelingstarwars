import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    UserName = Column(String(250), nullable=False)
    FavoriteID = Column(Integer, ForeignKey('Favorite'))

class Starships(Base):
    __tablename__ = 'Starships'
    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Model = Column(String(250), nullable=False)
    Pilot = Column(String(250), nullable=False)
    PeopleID =  Column(String(250), ForeignKey('People'))
    FavoriteID = Column(Integer, ForeignKey('Favorite'))

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Diameter = Column(String(250), nullable=False)
    Gravity = Column(String(250), nullable=False)
    PeopleID =  Column(String(250), ForeignKey('People'))
    FavoriteID = Column(Integer, ForeignKey('Favorite'))
    
class People(Base):
    __tablename__ = 'People'
    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Gender = Column(String(250), nullable=False)
    HomeWworld = Column(String(250), nullable=False)
    PlanetID = Column(Integer, ForeignKey('Planets'))
    FavoriteID = Column(Integer, ForeignKey('Favorite'))
    SpeciesID = Column(Integer, ForeignKey('Species'))
    FavoriteID = Column(Integer, ForeignKey('Favorite'))

class Species(Base):
    __tablename__ = 'Species'
    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Clasification = Column(String(250), nullable=False)
    Lenguage = Column(String(250), nullable=False)
    HomeWworld = Column(String(250), nullable=False)
    PlanetID = Column(Integer, ForeignKey('Planets'))
    FavoriteID = Column(Integer, ForeignKey('Favorite'))
    PeopleID =  Column(Integer, ForeignKey('People'))	



class Favorite(Base):
    __tablename__ = 'favorite'
    id  = Column(Integer, primary_key=True)
    PeopleID =  Column(Integer, ForeignKey('People'))
    PlanetID = Column(Integer, ForeignKey('Planets'))
    SpeciesID = Column(Integer, ForeignKey('Species'))
    StarshipID = Column(Integer, ForeignKey('Starships'))
    UserID = Column(Integer,ForeignKey('users'))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


