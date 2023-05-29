import pandas as pd
import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(user='your_username',
                              password='your_password',
                              host='your_host',
                              database='your_database')

# Define the SQL query to retrieve the data
query = "SELECT * FROM your_table"

# Execute the query and fetch the results
cursor = cnx.cursor()
cursor.execute(query)
data = cursor.fetchall()

# Get the column names from the cursor's description
column_names = [desc[0] for desc in cursor.description]

# Create a DataFrame using the fetched data and column names
df = pd.DataFrame(data, columns=column_names)

# Close the cursor and database connection
cursor.close()
cnx.close()

# Print the DataFrame
print(df)
