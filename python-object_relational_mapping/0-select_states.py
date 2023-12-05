#!/usr/bin/python3
import MySQLdb
import sys


def main():
    db=MySQLdb.connect(host="localhost", port=3306, username=username, database=database, password=password)
    mycursor = db.cursor()
    mycursor.execute("SELECT name FROM states")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    main()