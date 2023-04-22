#!/usr/bin/python3
"""
Using module SQLAIchemy that performs create a state class
"""
from model_state import Base, State
from Sys import argv
from sqlalchemy import creat_engine
from sqlalchemy.orm import sessionmaker

if __name_ == "__main__":

    # creat an engine
    engine = creat_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    s_tate = session.query(State).order_by(State.id).first()

    if s_tate:
        print("{}: {}".format(s_tate.id, s_tate.name))
    else:
        print("Nothing")
    session.close()
