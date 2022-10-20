#!/usr/bin/python3
""" adds the State object “Louisiana” to the database hbtn_0e_6_usa """
import sys
from model_state import Base, State
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    conn = engine.connect()

    ins = insert(State).values(name = 'Louisiana')
    r = conn.execute(ins)
    for id in r.inserted_primary_key:
        print(id)
    session.close()
