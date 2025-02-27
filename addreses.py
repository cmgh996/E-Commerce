# This file contains the routes for managing addresses in the Flask API.

from flask import Blueprint, jsonify, request
from models import Address
from session import session

address_api = Blueprint("routes", __name__)

@address_api.route("/addresses", methods=["GET"])
def get_addresses():
    """
    Retrieve all addresses from the database and return them in JSON format.
    """
    addresses = session.query(Address).all()

    addresses_in_dict_format = []

    for address in addresses:
        address_dict = {
            "id": address.id,
            "email_address": address.email_address,
            "user_id": address.user_id,
        }
        addresses_in_dict_format.append(address_dict)

    return jsonify(addresses_in_dict_format)
