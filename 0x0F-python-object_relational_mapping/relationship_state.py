#!/usr/bin/python3
"""
   1. Module that performs creates a states class based off of Base
   2. the ``State`` class which inherits from ``Base`` class
""" 

from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship
from splalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    __tablename__ = "states"
    id = Column(Integer, primay_Key=True)
    name = Column(String(128), nullable=False)
