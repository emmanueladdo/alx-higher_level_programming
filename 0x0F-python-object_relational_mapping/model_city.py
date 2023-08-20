#!/usr/bin/python3
"""
Class definition of a city
And an instance Base = declarative
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

from model_state import Base

Base = declarative_base()
"""Represents the base class for all tables"""


class City(Base):
    """Representation of a row in a city table"""
    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False
            )
