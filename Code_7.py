def insert_null_into_table(db_file, table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    query = f"INSERT INTO {table_name} VALUES (NULL)"
    cursor.execute(query)

    conn.commit()
    conn.close()
