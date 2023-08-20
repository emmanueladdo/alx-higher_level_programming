#!/usr/bin/python3
"""
Class definition of a State Class
And an instance Base = declarative
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
"""Represents the base class for all tables"""


class State(Base):
    """Representation of a row in a states table"""
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
