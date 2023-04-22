#!/usr/bin/python3
"""
This is a class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    City class that inherits from  Base

    Attributes:
        id: Id city
        name: NAME of the city
        state_id: State id
    """
    __tablename__ = "cities"
    id = Column(Integer, primay_Key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
