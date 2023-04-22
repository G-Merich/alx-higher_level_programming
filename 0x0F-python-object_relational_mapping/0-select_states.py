#!/usr/bin/python3
"""
this is python/MSQLdb project

"""

import MySQLdb
from sys import argv
def print_states(username, password, db_name):
    db = MySQLdb.connect(host="localhost",
                        user=username,
                        passwd=password,
                        db=db_name,
                        port=3306,
                        charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    outputs = cursor.fetchall()
    for output in outputs:
        print(output)

if __name__ == "__main__":
    credentials = argv
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    print_states(username, passwd, db_name)

