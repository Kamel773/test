def convert_sqlite_to_dataframe(database_file, table_name):
    # Connect to the SQLite database
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    
    # Fetch all rows from the table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    # Get the column names
    column_names = [description[0] for description in cursor.description]
    
    # Create a DataFrame from the fetched data
    df = pd.DataFrame(rows, columns=column_names)
    
    # Close the database connection
    cursor.close()
    connection.close()
    
    return df
