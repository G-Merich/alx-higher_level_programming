#!/usr/bin/python3
"""
1. Module that performs creates a states class based off of Base
2. the ``State`` class which inherits from ``Base`` class
"""
from model_state import Base, State
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
    state_update = session.query(State).filter_by(id='2').first()
    state_update.name = "New Mexico"
    # cimmit and close session
    session.commit()
    session.close()
