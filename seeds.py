# seeds.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

engine = create_engine('sqlite:///reviews.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add restaurants
restaurant1 = Restaurant(name="Best Burgers", price=2)
restaurant2 = Restaurant(name="Pizza Paradise", price=3)
restaurant3 = Restaurant(name="Sushi Haven", price=4)

session.add_all([restaurant1, restaurant2, restaurant3])
session.commit()

# Add customers
customer1 = Customer(first_name="Alice", last_name="Johnson")
customer2 = Customer(first_name="Bob", last_name="Smith")
customer3 = Customer(first_name="Charlie", last_name="Brown")

session.add_all([customer1, customer2, customer3])
session.commit()

# Add reviews
review1 = Review(star_rating=5, customer=customer1, restaurant=restaurant1)
review2 = Review(star_rating=4, customer=customer2, restaurant=restaurant1)
review3 = Review(star_rating=3, customer=customer1, restaurant=restaurant2)
review4 = Review(star_rating=5, customer=customer3, restaurant=restaurant3)

session.add_all([review1, review2, review3, review4])
session.commit()

print("Sample data added successfully!")



session.commit()
