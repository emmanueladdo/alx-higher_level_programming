#!/usr/bin/python3
"""
Print all City objs from db 'hbtn_0e_14_usa'
Sort in ascending order by cities.id
Display results as "<state name>: (<city id>) <city name>"
Script should take 3 args: username, pw, and db name
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1],
            argv[2],
            argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).join(State).all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
