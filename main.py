from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker

from models import db, User, Address

engine = create_engine("sqlite:///example.db")

# Create the tables in the database
db.metadata.create_all(engine)

# Set up the session
Session = sessionmaker(bind=engine)
session = Session()

# Create a new user instance
#new_user = User(name='Carlos', fullname='Carlos Guzman', nickname='El Chapo')

# Add the new user to the session
#session.add(new_user)

# Commit the transaction to persist the new user
#session.commit()

# Optionally, query the database to confirm the user is saved
# saved_user = session.query(User).filter_by(name='Carlos').first()
# # print(saved_user)
# if saved_user:
#     new_address = Address(email_address="carlostunenuco69@gmail.com", user=saved_user)
#     session.add(new_address)
#     session.commit()

# Query the database to confirm the address is saved
# saved_address = session.query(Address).filter_by(email_address="carlostunenuco69@gmail.com").first()

# print("user_name:", saved_address.user.name)


carlos = session.query(User).filter_by(name="Carlos").first()

print(carlos.addresses[0].email_address)