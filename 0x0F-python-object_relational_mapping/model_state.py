#!/usr/bin/python3
"""
This file contains class definition of a state and an instance
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create a base class
Base = declarative_base()


# Define a State class that inherits from Base
class State(Base):
    """Represents a state in the database"""

    # Link to MySQL table states
    __tablename__ = 'states'

    # define the columns of the table
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
