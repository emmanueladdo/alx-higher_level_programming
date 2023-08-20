#!/usr/bin/python3
"""
lists all the cities from the database
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                      FROM cities INNER JOIN states
                      ON cities.state_id = states.id""")
    for city in cursor.fetchall():
        print(city)
    cursor.close()
    db.close()
