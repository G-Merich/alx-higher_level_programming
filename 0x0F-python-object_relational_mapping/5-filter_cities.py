#!/usr/bin/python3
"""
This is an argument statement
"""
import MySQLdb
from sys import argv

if (len(argv) < 5):
    pass
else:
    try:
        connector = MySQLdb.connect(host="localhost", 
                                    port=3306, 
                                    user=argv[1],
                                    passwd=argv[2],
                                    db=argv[3],
                                    charset="utf8"
                                    )
    except IndexError:
        pass
    cur = connector.cursor()
    cur.execute("SELECT cities.name\
                FROM `cities`\
                JOIN `states` ON state_id=states.id\
                WHERE states.name=(%s)\
                ORDER BY cities.id", [argv[4]])
    results = cur.fetchall()
    cities = ""
    for result in results:
        for result2 in result:
            cities += (result2) + ", "
    print(cities[:-2])
    cur.close()
    connector.close()
