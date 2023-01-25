#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa.
        Usage: ./2-my_filter_states.py <mysql username> \
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
    cur.execute("SELECT * FROM states WHERE name = BINARY '{}'".format(arg[4]))
    for state in cur.fetchall():
        print(state)
