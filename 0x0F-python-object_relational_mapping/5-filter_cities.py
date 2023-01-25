#!/usr/bin/python3
""" Lists all cities of a state from the database hbtn_0e_4_usa.
        Usage: ./5-filter_cities.py <mysql username> \
                                        <mysql password> \
                                        <database name>  \
                                        <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    db = MySQLdb.connect(user=arg[1], passwd=arg[2], db=arg[3])
    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities as c \
                JOIN states as s ON c.state_id = s.id \
                WHERE s.name = BINARY %s \
                ORDER BY c.id", (arg[4],))
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
    cur.close()
    db.close()
