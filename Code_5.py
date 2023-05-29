import sqlite3
import json

def get_table_as_json(db_path, table_name):
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute the query to select all rows from the table
    cursor.execute(f"SELECT * FROM {table_name}")

    # Fetch all rows from the cursor
    rows = cursor.fetchall()

    # Get the column names from the cursor description
    columns = [desc[0] for desc in cursor.description]

    # Create a list to store the JSON objects
    data = []

    # Iterate over the rows and convert each row to a dictionary
    for row in rows:
        row_dict = dict(zip(columns, row))
        data.append(row_dict)

    # Convert the data list to JSON
    json_data = json.dumps(data)

    # Close the database connection
    conn.close()

    return json_data

# Example usage
database_path = "example.db"
table_name = "employees"

json_result = get_table_as_json(database_path, table_name)
print(json_result)
