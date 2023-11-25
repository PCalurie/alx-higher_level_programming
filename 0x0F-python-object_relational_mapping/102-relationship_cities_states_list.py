#!/usr/bin/python3
"""Script Lists all the City objects from the database hbtn_0e_101_usa"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        # Use the state relationship to access the State object
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close session
    session.close()