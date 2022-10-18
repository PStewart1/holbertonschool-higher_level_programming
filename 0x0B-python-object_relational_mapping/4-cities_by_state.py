#!/usr/bin/python3
""" a script that  lists all cities,
with their states, from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    try:
        cur.execute(
            '''SELECT c.id, c.name, s.name
            FROM cities AS c
            LEFT JOIN states AS s
            ON c.state_id = s.id
            ORDER BY c.id ASC''',
            )
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
