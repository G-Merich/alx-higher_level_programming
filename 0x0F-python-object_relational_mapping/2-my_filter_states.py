#!/usr/bin/python3
"""
If the arguement isn't working, print result
"""

import MySQLdb
from sys import argv

if (len(argv) < 4 or len(argv) > 5):
    raise IndexError("Arguments must be five")
else:
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{:s}'".format(argv[4]))
    results = cursor.fetchall()
    for result in results:
        print(result)
    db.close()

