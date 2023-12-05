#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    db=MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    mycursor = db.cursor()
    x = mycursor.execute("SELECT * FROM states ORDER BY states.id")
    for i in x:
        print(mycursor.fetchall())
