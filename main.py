# This file contains the main application code for the Flask API.

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from models import db, User, Address

from flask import Flask, request, jsonify
from addreses import address_api
from session import session

# Create a new Flask application
api = Flask(__name__)
# Register the address_api blueprint
api.register_blueprint(address_api)


@api.route("/users", methods=["GET"])
def get_users():
    """
    Retrieve all users from the database and return them in JSON format.
    """
    users = session.query(User).all()

    usuarios_en_formato_diccionario = []

    for user in users:
        user_dict = {
            "id": user.id,
            "name": user.name,
            "fullname": user.fullname,
            "nickname": user.nickname,
        }
        usuarios_en_formato_diccionario.append(user_dict)

    return jsonify(usuarios_en_formato_diccionario)

@api.route("/users", methods=["POST"])
def create_user():
    """
    Create a new user in the database with the provided data.
    """
    data = request.get_json()
    new_user = User(name=data["name"], fullname=data["fullname"], nickname=data["nickname"])
    session.add(new_user)
    session.commit()
    return jsonify({"message": "User created successfully"}), 201


if __name__ == "__main__":
    api.run(port=5000, debug=True)
