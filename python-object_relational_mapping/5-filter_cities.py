#!/usr/bin/python3
"""
filter cities from database
Using hbtn_0e_4_usa database
safe fromSQL injection
                  
"""
import MySQLdb
from sys import argv

names = argv[4]
if __name__ == "__main__":
    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=argv[1],
                        password=argv[2],
                        db=argv[3])
    myc = db.cursor()
    myc.execute("SELECT cities.name "
                "FROM cities join states "
                "ON states.id = cities.state_id "
                "AND states.name = %s "
                "ORDER BY cities.id", (names, ))
    fet = myc.fetchall()
    idx = 0
    for x in fet:
        if idx != 0:
            print(',', end=' ')
        print(x[0], end='')
        idx += 1
    print('')
    db.close()
