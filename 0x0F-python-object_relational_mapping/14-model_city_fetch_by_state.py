#!/usr/bin/python3
# Print all City objs from db 'hbtn_0e_14_usa'
# Sort in ascending order by cities.id
# Display results as "<state name>: (<city id>) <city name>"
# Script should take 3 args: username, pw, and db name

from sys import argv
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    State.cities = relationship('City', back_populates='state')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    result = session.query(City).order_by(City.id.asc()).all()
    for row in result:
        print('{}: ({}) {}'.format(row.state.name, row.id, row.name))
