#!/usr/bin/python3
"""
Module that performs creates a city object print
"""
from model_state import Base, State
from model_city import City
from Sys import argv
from sqlalchemy import creat_engine
from sqlalchemy.orm import sessionmaker

if __name_ == "__main__":

    # creat an engine
    engine = creat_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create a configurd a "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session 
    session = Session()
    Base.matadata.creat_all(engine)
    
    city = session.query(State, City).jion(City).order_by(City.id)
    fro state, city in city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    # close session
    session.close()
