#!/usr/bin/python3
"""lists states begining with N from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connect"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2], db=argv[3])
    """cursor"""
    mycursor = db.cursor()
    """execute"""
    mycursor.execute("SELECT * FROM states WHERE\
                      name LIKE 'N%' ORDER BY states.id")
    x = mycursor.fetchall()
    for i in x:
        print(i)
    db.close()
    x.close()
