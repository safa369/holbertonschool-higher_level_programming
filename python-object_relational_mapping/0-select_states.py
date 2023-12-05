#!/usr/bin/python3
"""lists all states from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db=MySQLdb.connect(host="localhost", port=3306, user=argv[1], password=argv[2], db=argv[3])
    mycursor = db.cursor()
    x = mycursor.execute("SELECT * FROM states ORDER BY states.id")
    for i in range(x):
        print(mycursor.fetchone())
