#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa.
    Usage: ./4-cities_by_state.py <mysql username> \
            <mysql password> \
            <database name>
"""

import sys
import MySQLdb


if __name__ == "__main__":
    arg = sys.argv
    db = MySQLdb.connect(user=arg[1], passwd=arg[2], db=arg[3])
    cur = db.cursor()
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    for state in cur.fetchall():
        print(state)
