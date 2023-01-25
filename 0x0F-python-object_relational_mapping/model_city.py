#!/usr/bin/python3
"""
File that contains the class definition of a City.
Using Python Object Relational Mapping.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    A subclass of Base,
    Links to the MySQL table states

    Attributes:
                id(str) - Reps a column of auto generated unique integer
                name (sqlalchemy.String) - The City's name
                state_id (sqlalchemy.Integer) - The City's state id.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey("states.id")
