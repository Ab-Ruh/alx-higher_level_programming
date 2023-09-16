#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <database> <state_name>".format(
                sys.argv[0]))
        sys.exit(1)

    # Extract the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Execute the SQL query to fetch states matching the user input
        query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all the results
        states = cursor.fetchall()

        # Print the results
        for state in states:
            print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)