#!/usr/bin/python3
"""prints all city objects from the database"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    engine=create_engine('mysql+mysqldb://{}: {}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),  pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cit = session.query(City).join(State).order_by(City.id.asc()).all()

    for c in cit:
        print('{}: ({}) {}'
              .format(c.State.name, c.City.id, c.City.name))
    session.commit()
    session.close()

 
if __name__ == '__main__':
    main()