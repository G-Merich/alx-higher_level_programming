#!/usr/bin/python3
"""
This is an argument statement
"""
import MySQLdb
from sys import argv

if (len(argv) == 4):
    try:
        connector = MySQLdb.connect(
                                    host="localhost",
                                    port=3306,
                                    user=argv[1],
                                    passwd=argv[2],
                                    db=argv[3],
                                    charset="utf8"
                                    )
    except IndexError:
        pass
    cur = connector.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities INNER JOIN states ON cities.state_id = states.id")
    results = cur.fetchall()
    for result in results:
        print(result)
    connector.close()

