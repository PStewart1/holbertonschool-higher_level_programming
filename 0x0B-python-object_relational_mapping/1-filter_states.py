#!/usr/bin/python3
""" a script that lists all states starting with an 'N' """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    try:
        cur.execute(
            "SELECT * FROM states WHERE ASCII(name) = 78 ORDER BY id ASC")
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: %s" % str(e))
    for row in rows:
        print(row)
    cur.close()
    db.close()
