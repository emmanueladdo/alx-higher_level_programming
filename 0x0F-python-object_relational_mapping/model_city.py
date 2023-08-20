#!/usr/bin/python3
"""
Class definition of a city
And an instance Base = declarative
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

Base = declarative_base()
"""Represents the base class for all tables"""


class City(Base):
    """Represents a row in a cities table"""
    __tablename__ = "cities"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(length=128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
    state = relationship('State', back_populates='cities')
