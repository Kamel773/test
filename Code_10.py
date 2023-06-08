import sqlite3

def detection(db_file, table_name, row_id):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Delete the row from the table
    delete_query = f"DELETE FROM {table_name} WHERE rowid = ?"
    cursor.execute(delete_query, (row_id,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print(f"Row with rowid {row_id} deleted successfully from {table_name}.")


# Usage example
db_file = "example.db"  # Path to your SQLite database file
table_name = "my_table"  # Name of the table you want to delete the row from
row_id = 3  # ID of the row you want to delete

detection(db_file, table_name, row_id)
