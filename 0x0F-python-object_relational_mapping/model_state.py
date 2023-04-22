#!/usr/bin/python3
"""
    This is a class file
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()



class State(Base):
    """
        This class will contain class attribute
    """
    
    __tablename__ = "states"

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

#if __name__ == "__main__":

