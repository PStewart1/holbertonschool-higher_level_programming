#!/usr/bin/python3
""" a script that takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    try:
        cur.execute(
            '''SELECT c.name
            FROM cities AS c
            LEFT JOIN states AS s
            ON c.state_id = s.id
            WHERE s.name = %s
            ORDER BY c.id ASC''',
            (argv[4],))
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: %s" % str(e))
    results = []
    for row in rows:
        for col in row:
            results.append(col)
    print(*results, sep=', ')
    cur.close()
    db.close()
