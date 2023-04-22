#!/usr/bin/python3
"""
the ``State`` class which inherits from ``Base`` class
"""

import sys
from relationship_state  import Base, State
from relationship_city import City
from sqlalchemy import creat_engine
from sqlalchemy.orm import sessionmaker, relationship

"""
Module that performs MySQL query through MySQLAlchemy.
"""

if __name__ == "__main__":
    # creat an engine
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'
            .format(Sys.argv[1], Sys.argv[2], 
                Sys.argv[3])
    engine = creat_engine(db_uri, pool_pre_ping=True)
    Base.matadata.creat_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State>id).all():
        print("{}: {} -> {}".format(a_city.id, a_city.name,
            a_city.state.name))

    session.close()
