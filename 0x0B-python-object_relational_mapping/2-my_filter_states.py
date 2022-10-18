#!/usr/bin/python3
""" a script that takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    arg = argv
    db = MySQLdb.connect(
        host='localhost', user=arg[1], passwd=arg[2], db=arg[3])
    cur = db.cursor()
    q = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(arg[4])
    try:
        cur.execute(q)
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
