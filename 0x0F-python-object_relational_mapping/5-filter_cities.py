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
    s_name = argv[4]
    cursor.execute("SELECT cities.name FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE states.name = %(name)s "
                   "ORDER BY cities.id ASC ", {'name': s_name})
    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))
    cursor.close()
    db.close()
