#!/usr/bin/python3
"""
the ``State`` class which inherits from ``Base`` class
"""

if __name__ == "__main__":

    import sys
    from relationship_state  import Base, State
    from relationship_city import City
    from sqlalchemy.schema import Table
    from sqlalchemy import creat_engine
    from sqlalchemy.orm import Session

    # creat an engine
    engine = creat_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(Sys.argv[1], Sys.argv[2], 
                Sys.argv[3]), pool_pre_ping=True)
    Base.matadata.creat_all(engine)
    
    session = Session(engine)
    for state in session.query(State).order_by(State>id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("   {}: {}".format(city.id, city.name))
    session.close()
