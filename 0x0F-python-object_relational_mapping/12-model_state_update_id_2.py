#!/usr/bin/python3
"""
changes the State object with the name passed as
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

    session.query(State).filter(State.id == 2).update(
        {State.name: 'New Mexico'},
        synchronize_session=False
    )
    session.commit()
