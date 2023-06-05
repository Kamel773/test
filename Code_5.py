def get_table_as_json(db_file, table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    if not rows:
        return '[]'

    column_names = [desc[0] for desc in cursor.description]
    results = []
    for row in rows:
        row_data = {}
        for idx, col in enumerate(column_names):
            row_data[col] = row[idx]
        results.append(row_data)
    conn.close()
    return json.dumps(results)
