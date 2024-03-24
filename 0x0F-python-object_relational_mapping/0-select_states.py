#!/usr/bin/python3
"""lists states in a database"""
import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = db.cursor

cur.execute("SELECT * FROM states ORDER BY states.id ASC")
states = cur.fetchall()
for state in states:
    print(state)

if __name__ == "__main__":
    import MySQLdb
