#!/usr/bin/python3
"""lists states input by user"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    nams = argv[4]
    """connect"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2], db=argv[3])
    """cursor"""
    mycursor = db.cursor()
    """execute"""
    mycursor.execute("SELECT * FROM states WHERE name = %s \
                     ORDER BY states.id", (nams,))
    x = mycursor.fetchall()
    for state in x:
        if state[1] == nams:
            print(state)
    db.close()
