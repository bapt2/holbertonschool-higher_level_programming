#!/usr/bin/python3
""" lists all states object from database hbtn_0e_6_usa"""

from model_state import State, Base
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, database))

    result = engine.execute(text("SELECT * FROM states;"))
    for row in result.fetchall():
        print("{}: {}".format(row[0], row[1]))
