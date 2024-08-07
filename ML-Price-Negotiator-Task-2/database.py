from sqlalchemy import create_engine
from models import Base, Product, User, Review, Order
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def insert_product(product_id, product_name, category, discounted_price, actual_price, discount_percentage, rating, rating_count, about_product, user_id, user_name, review_id, review_title, review_content, img_link, product_link):
    product = Product(
        product_id=product_id, product_name=product_name, category=category, discounted_price=discounted_price,
        actual_price=actual_price, discount_percentage=discount_percentage, rating=rating, rating_count=rating_count,
        about_product=about_product, user_id=user_id
    )
    session.add(product)
    session.commit()

def insert_order(product_id, user_id, price):
    order = Order(product_id=product_id, user_id=user_id, price=price)
    session.add(order)
    session.commit()

def insert_user(user_id, user_name, email):
    user = User(user_id=user_id, user_name=user_name, email=email)
    session.add(user)
    session.commit()

def get_product_info(product_id):
    return session.query(Product).filter_by(product_id=product_id).first()

def get_order_info(order_id):
    return session.query(Order).filter_by(order_id=order_id).first()

def get_user_info(user_id):
    return session.query(User).filter_by(user_id=user_id).first()
