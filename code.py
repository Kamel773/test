import pyodbc

def query_ages_less_than_twenty():
    # Connection parameters
    server = 'your_server_name'
    database = 'your_database_name'
    username = 'your_username'
    password = 'your_password'
    
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
