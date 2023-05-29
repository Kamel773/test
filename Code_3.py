from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy engine
engine = create_engine('your_database_connection_string')

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

# Define your table as a SQLAlchemy model
class YourTable(Base):
    __tablename__ = 'your_table_name'
    id = Column(Integer, primary_key=True)
    # Define other columns here

# Count the number of rows in the table
row_count = session.query(func.count()).select_from(YourTable).scalar()

print("Total rows:", row_count)
