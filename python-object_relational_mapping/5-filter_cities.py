#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    connection = MySQLdb.connect(user=username, passwd=password,
                                 db=database, host="localhost",
                                 port=3306)

    cursor = connection.cursor()
    request = "SELECT cities.name FROM cities JOIN states \
    ON cities.stade_id = states.id WHERE state.name = %s\
        ORDER BY cities.id"
    cursor.execute(request, (state_name,))

    cityList = cursor.fetchall()

    print(", ".join(city[0] for city in cityList))

    cursor.close()
    connection.close()
