
def insert_data(db_config, table_name, data):
    """Inserts data into a MySQL database.
    
    Args:
        db_config (dict): A dictionary containing the database configuration.
        table_name (str): The name of the table to insert data into.
        data (dict): A dictionary containing the data to insert.
    """
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Create the SQL query
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    sql = "INSERT INTO %s (%s) VALUES (%s)" % (table_name, columns, placeholders)
    
    # Execute the query
    cursor.execute(sql, list(data.values()))
    
    # Commit the changes
    conn.commit()
