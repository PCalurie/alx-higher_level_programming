#!/usr/bin/python3
"""
This script lists all states from a database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to a MySQL server
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
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all records
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor
    cursor.close()

    # Close the connection
    db.close()
