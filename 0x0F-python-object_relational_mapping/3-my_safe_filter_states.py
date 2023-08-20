#!/usr/bin/python3
"""
lists all the states from the database
that matches with argument passed
in a safe way
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
    cursor.execute("SELECT * FROM states "
                   "WHERE name = %(name)s "
                   "ORDER BY id ASC", {'name': s_name})
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
