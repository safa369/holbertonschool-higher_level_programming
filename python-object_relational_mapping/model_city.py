#!/usr/bin/python3
"""file contain th class definition of a City"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import State


Base = declarative_base()


class City(Base):
    """class that define a table named city
    Attribute:
        id: integer
        name: string
        states_id: foreign key of states.id"""
    __tablename__ = "cities"
    id = (Column(Integer, nullable=False, primary_key=True))
    name = (Column(String(128), nullable=False))
    state_id = (Column(Integer, ForeignKey(State.id)))
