from sqlalchemy import create_engine, MetaData, Table

def get_columns_and_types(database_uri, table_name):
    engine = create_engine(database_uri)
    meta = MetaData()

    # Load the table from the database
    table = Table(table_name, meta, autoload_with=engine)

    # Create a dictionary to store column names and types
    column_data = {}

    # Populate the dictionary with column name as key and type as value
    for column in table.columns:
        column_data[column.name] = str(column.type)

    return column_data
