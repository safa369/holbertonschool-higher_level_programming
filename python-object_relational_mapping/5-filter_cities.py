#!/usr/bin/python3
""" filter cities from databse"""
import MySQLdb
from sys import argv

name = argv[4]


if __name__ == "__main__":
    """connect"""
    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=argv[1],
                        password=argv[2],
                        db=argv[3])
    """cursor"""
    myc = db.cursor()
    """execute"""
    myc.execute("SELECT cities.name "
                "FROM cities join states "
                "ON states.id = cities.state_id "
                "WHERE states.name = %s "
                "ORDER BY cities.id", (name,))
    """fetchall"""
    fet = myc.fetchall()
    for x in fet:
        if x[0] == name:
            print(x[0])
    """close"""
    db.close()
