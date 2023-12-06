#!/usr/bin/python3
"""lists all cities from databse"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=argv[1],
                        password=argv[2],
                        db=argv[3])
    myc = db.cursor()
    myc.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities join states ON states.id=cities.id "
                "ORDER BY cities.id")
    fet = myc.fetchall()
    for x in fet:
        print(x)
    db.close()
