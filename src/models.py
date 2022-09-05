import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

favorits_planets = Table('favorits_planets',Base.metadata ,
    
    Column('user_id', Integer(), ForeignKey('user.id'), primary_key=True),
    Column('planets_id', Integer(), ForeignKey('planets.id'), primary_key=True),
    
)

favorits_characters = Table('favorits_characters',Base.metadata,
    
   Column('user_id', Integer(), ForeignKey('user.id'), primary_key=True),                                         
   Column('characters_id', Integer(), ForeignKey('characters.id'), primary_key=True))



class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False , unique=True)
    mail = Column(String(120), nullable=False , unique=True)
    password = Column(String(80), nullable=False , unique=False)
    user_name = Column(String(20), nullable=False , unique=True)

    def to_dict(self):
        return {}

 

class Characters(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False , unique=True)
    eye_color = Column(String(250), nullable=False , unique=False )
    favorits_characters = relationship('User', secondary = favorits_characters )
    def to_dict(self):
        return {}

  
    

class Planets(Base):
    __tablename__ = 'planets'
    
    id = Column(Integer, primary_key=True)
    population = Column(Integer , nullable=False )
    terrain = Column(Integer , nullable=False )
    favorits_planets = relationship('User', secondary = favorits_planets )
   
    def to_dict(self):
        return {}










   
render_er(Base, 'diagram.png')