#!/usr/bin/python3
"""
Creates  the State Califonia
with city San Fracisco from the
Database hbtn_0e_100_usa
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1],
            argv[2],
            argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(City).join(State).order_by(City.id.asc())
    for city in q.all():
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
