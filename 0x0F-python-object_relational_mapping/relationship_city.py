#!/usr/bin/python3
"""
This is a class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey, text
from relationship_state import Base

class City(Base):
    """
        the ``City`` class which inherits from ``Base`` class.
    """
    __tablename__ = "cities"
    id = Column(Integer, primay_Key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
