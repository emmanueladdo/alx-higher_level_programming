#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
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
    results = session.query(State).filter(State.name.like('%a%'))
    for instance in results:
        session.delete(instance)
    session.commit()
    session.close()
