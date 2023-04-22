#!/usr/bin/python3
"""
Module that performs creates a city object print
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
    new_city = City(name='San Francisco')
    new = State(name+'California')
    new.cities.append(new_city)
    session.add_all([new, new_city])
    session.commit()
    session.close()
