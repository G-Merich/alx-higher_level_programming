#!/usr/bin/python3

"""
mydb = mysql.connector.connect(
    host="0-select_states.py",
    user="username",
    password="password",
    database="hbtn_0e_0_usa"
)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
