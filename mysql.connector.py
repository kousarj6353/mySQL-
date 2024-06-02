import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # replace with your username
            password='K2005@kousar#',  # replace with your password
            database='mfi_table'  # replace with your database name
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            # Create a cursor object using the cursor() method
            cursor = connection.cursor()

            # Execute SQL query to count rows in a table
            cursor.execute("SELECT COUNT(*) FROM your_table")  # replace with your table name
            row_count = cursor.fetchone()
            print(f"Row count: {row_count[0]}")

            # Execute SQL query to get sample rows
            cursor.execute("SELECT * FROM your_table LIMIT 3")  # replace with your table name
            rows = cursor.fetchall()
            print("Sample rows:")
            for row in rows:
                print(row)

            # Close the cursor and connection
            cursor.close()
            connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

if _name_ == "_main_":
    connect_to_database()