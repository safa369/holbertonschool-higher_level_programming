#!/usr/bin/python3
""" filter cities from databse"""
import MySQLdb
from sys import argv

names = argv[4]


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
                "FROM states join cities "
                "ON states.id = cities.state_id "
                "WHERE states.name = %s "
                "ORDER BY cities.id", (names,))
    """fetchall"""
    fet = myc.fetchall()
    for x in fet:
            print(x)
    """close"""
    db.close()
