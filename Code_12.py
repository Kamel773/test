import sqlite3

def insert_null(db_name, table_name, column_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO {} ({}) VALUES (?)".format(table_name, column_name), (None,))
    conn.commit()
    conn.close()
