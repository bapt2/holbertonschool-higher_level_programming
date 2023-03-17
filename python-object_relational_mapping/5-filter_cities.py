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
    request = "SELECT cities.name, states.name\
        FROM cities, states WHERE cities.state_id = states.id\
        ORDER BY cities.id"
    cursor.execute(request, (state_name,))

    cityList = cursor.fetchall()

    for city in cityList:
        print(city)

    cursor.close()
    connection.close()
