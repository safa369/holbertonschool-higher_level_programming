#!/usr/bin/python3
"""prints all city objects from the database"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine=create_engine('mysql+mysqldb://{}: {}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()

    cit = session.query(City, State).join(State, State.id == City.state_id)\
        .order_by(City.id.asc()).all()

    for c in cit:
        print('{}: ({}) {}'
              .format(c.State.name, c.City.id, c.City.name))
