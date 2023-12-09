#!/usr/bin/python3
"""list the state with the name passed as argument"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name='Louisiana')

    session.add(louisiana)
    session.commit()

    print("{}".format(louisiana.id))
