#!/usr/bin/python3
"""
A script that takes in an argument and
displays all value in the states table
of where name matches the argument.
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    # Connect database using command-line arguments
    my_db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306
        )

    # Create cursor obj to interact with database
    my_cursor = my_db.cursor()

    # Execute a SELECT query to fetch data
    my_cursor.execute(
        """
        SELECT * FROM states  WHERE name LIKE BINARY '{}'
        ORDER BY states.id ASC
        """.format(argv[4])
        )

    # fetch all the data returned by the query
    my_data = my_cursor.fetchall()

    # Iterate through the fetched data and print each row
    for row in my_data:
        print(row)

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()
