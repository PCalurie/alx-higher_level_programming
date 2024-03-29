#!/usr/bin/python3
"""
This script lists all cities from database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],  # username
        passwd=sys.argv[2],  # password
        db=sys.argv[3],  # database name
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    # Fetch all records
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor
    cursor.close()

    # Close connection
    db.close()
