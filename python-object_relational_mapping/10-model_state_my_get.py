#!/usr/bin/python3
"""list the state with the name passed as argument"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    name = (argv[4], )
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == name)\
        .order_by(State.id.asc())
    if not states:
        print ("Not found")
    else:
        for state in states:
            print("{}".format(state.id))
