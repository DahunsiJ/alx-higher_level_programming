#!/usr/bin/python3
""" File that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A subclass of Base,
    Links to the MySQL table states

    Attributes:
                id - Reps a column of auto generated unique integer
                name - Reps a column of a string with max 128 chars
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
