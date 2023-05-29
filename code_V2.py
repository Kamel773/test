import pyodbc
import configparser

def query_ages_less_than_twenty():
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Extract the SQL Server connection parameters
    server = config.get('SQLServer', 'server')
    database = config.get('SQLServer', 'database')
    username = config.get('SQLServer', 'username')
    password = config.get('SQLServer', 'password')

    # Establish a connection
    conn = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')

    # Create a cursor object
    cursor = conn.cursor()

    try:
        # Execute the query
        cursor.execute('SELECT * FROM YourTableName WHERE age < 20')

        # Fetch all rows
        rows = cursor.fetchall()

        # Print the rows
        for row in rows:
            print(row)

    except pyodbc.Error as e:
        # Handle any errors that occur during execution
        print(f"An error occurred: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
