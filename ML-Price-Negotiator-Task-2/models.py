from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    category = Column(String)
    discounted_price = Column(Float)
    actual_price = Column(Float)
    discount_percentage = Column(Float)
    rating = Column(Float)
    rating_count = Column(Integer)
    about_product = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship("User", backref="products")
    reviews = relationship("Review", backref="product")

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    email = Column(String)
    orders = relationship("Order", backref="user")
    reviews = relationship("Review", backref="user")

class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, primary_key=True)
    review_title = Column(String)
    review_content = Column(String)
    img_link = Column(String)
    product_link = Column(String)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    price = Column(Float)
