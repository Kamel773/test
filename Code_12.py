import sqlite3

def insert_null(db_name, table_name, column_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table_name} ({column_name}) VALUES (?)", (None,))
    conn.commit()
    conn.close()
