import sqlite3

# Example list
my_list = [1, 2, 3, 4, 5]

# Connect to the database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create a placeholder string for the list elements
placeholders = ', '.join('?' for _ in my_list)

# Form the SQL query with the placeholders
query = f"SELECT * FROM your_table WHERE your_column IN ({placeholders})"

# Execute the query with the list as a parameter
cursor.execute(query, my_list)

# Fetch the results
results = cursor.fetchall()

# Do something with the results
for row in results:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()
