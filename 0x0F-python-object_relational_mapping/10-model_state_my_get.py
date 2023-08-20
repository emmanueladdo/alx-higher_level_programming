#!/usr/bin/python3
"""
Prints the State object with the name passed as
argument from the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    state_found = False
    for state in session.query(State).filter(
            State.name == sys.argv[4]).order_by(
            State.id):
        print(state.id)
        state_found = True

    if not state_found:
        print("Not found")

    session.close()
