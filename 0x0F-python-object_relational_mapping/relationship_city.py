#!/usr/bin/python3
"""
Class definition of a city
And an instance Base = declarative
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """
    City class that inherits from Base.
    Represents a city in a state.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
