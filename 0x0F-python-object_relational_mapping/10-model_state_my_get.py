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

    state_name = argv[4]
    check = map(lambda x: x.isalpha() or (x in (' ', '%', '_')), state_name)
    if not all(check):
        state_name = ''
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    results = session.query(State).filter(State.name == state_name).first()
    if results is None:
        print('Not found')
    else:
        print('{}'.format(results.id))
