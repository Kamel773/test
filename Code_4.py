import pymysql

def execute_sql_script(filename):
    # Connect to the database
    conn = pymysql.connect(host='localhost', user='your_username', password='your_password', db='your_database')

    # Create a cursor object
    cursor = conn.cursor()

    # Read the SQL script file
    with open(filename, 'r') as file:
        sql_script = file.read()

    # Execute the SQL script
    try:
        cursor.execute(sql_script)
        conn.commit()
        print("SQL script executed successfully.")
    except Exception as e:
        conn.rollback()
        print("Error executing SQL script:", str(e))

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Specify the path to your SQL script file
sql_script_file = 'path/to/your/sql_script.sql'

# Call the function to execute the SQL script
execute_sql_script(sql_script_file)
