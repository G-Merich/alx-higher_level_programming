#!/usr/bin/python3
"""
Working on table
"""

import MySQLdb
from sys import argv

if (len(argv) < 4):
    pass
else:
    conn = MySQLdb.connect(host="localhost",
                            user=argv[1],
                            passwd=argv[2],
                            db=argv[3],
                            port=3306,
                            charset="utf8")
    current = conn.cursor()
    current.execute("SELECT * FROM states")
    results = current.fetchall()
    for result in results:
        if (result[1][0] == "N"):
            print(result)
    conn.close()
