#!/usr/bin/python3
"""
lists all the states from the database
with the name starting Upper N
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
    cursor.execute("SELECT * FROM states "
                   "WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()