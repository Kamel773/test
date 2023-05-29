import pyodbc

# Set up connection parameters
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 17 for SQL Server}'  # Change the driver if necessary

# Create a connection string
connection_string = f'server={server};database={database};uid={username};pwd={password};driver={driver}'

try:
    # Establish the connection
    conn = pyodbc.connect(connection_string)

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a sample query
    cursor.execute('SELECT * FROM your_table_name')

    # Fetch and print the result
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {str(e)}")
