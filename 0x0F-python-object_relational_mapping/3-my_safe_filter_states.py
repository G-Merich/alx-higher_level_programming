#!/usr/bin/python3
"""
This is an argument statement
"""

import MySQLdb
from sys import argv

if (len(argv) < 5 or len(argv) > 5):
    pass
try:
    conn = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
        )
except:
    exit(1)
cur = conn.cursor()
cur.execute("SELECT * FROM `states`\
            WHERE `name`=(%s) ORDER BY `id` ASC", (argv[4],))
results = cur.fetchall()
for result in results:
    print(result)
cur.close()
conn.close()
