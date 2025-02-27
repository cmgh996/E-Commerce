from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db

engine = create_engine("sqlite:///example.db")

# Create the tables in the database
db.metadata.create_all(engine)

# Set up the session
Session = sessionmaker(bind=engine)
session = Session()