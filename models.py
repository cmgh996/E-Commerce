# This file contains the SQLAlchemy models for the Flask API.

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

db = declarative_base()

class User(db):
    """
    Represents a user in the database.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"

class Address(db):
    """
    Represents an address in the database.
    """
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)

    # Foreign key to the User table
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="addresses")

    def __repr__(self):
        return f"<Address(email_address={self.email_address})>"
