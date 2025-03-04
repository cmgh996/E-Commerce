# This file contains the SQLAlchemy models for the Flask API.
import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, date, time, timezone

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
    user = relationship(User, backref="addresses")

    def __repr__(self):
        return f"<Address(email_address={self.email_address})>"

class Product(db):
    """
    Represents a product in the database.
    """
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    model = Column(String)
    weapon = Column(String)

    def __repr__(self):
        return f"<Product(name={self.name}, description={self.description}, price={self.price}, stock={self.stock}, model={self.model}, weapon={self.weapon})>"

class Cart(db):
    """
    Represents the cart of a buyer in the database.
    """
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True)
    creation_date = Column(Date, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Cart(creation_date={self.creation_date}, relation_cart_item={self.relation_cart_item})>"

class CartItem(db):
    """
    Represents the cart items in the database.
    """
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)

    cart_id = Column(Integer, ForeignKey("carts.id"))
    cart = relationship(Cart, backref="cart_items")

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship(Product)


    def __repr__(self):
        return f"<CartItem(relation_cart={self.relation_cart}, relation_product={self.relation_product}, quantity={self.quantity})>"

class Order(db):
    """
    Represents the order in the database.
    """
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    creation_date = Column(Date, default=datetime.now(timezone.utc))
    total_amount = Column(Integer)
    status = Column(String)
    client_info = Column(String)

    def __repr__(self):
        return f"<Order(creation_date={self.creation_date}, total_amount={self.total_amount}, status={self.status}, client_info{self.client_info}, relation_order_items{self.relation_order_items})>"

class OrderItem(db):
    """
    Represents the order items in the database.
    """
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    price = Column(Integer)

    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship(Order, backref="orders")

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship(Product)

    def __repr__(self):
        return f"<OrderItem(relation_order={self.relation_order}, relation_product={self.relation_product}, quantity{self.quantity}, price{self.price})>"

