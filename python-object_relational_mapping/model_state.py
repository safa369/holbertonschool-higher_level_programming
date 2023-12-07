#!/usr/bin/python3
"""create table"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """class of a table named states
    attribute:
        id: integer.
        name: max 128 charac """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
