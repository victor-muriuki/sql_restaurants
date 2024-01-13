# debug.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

engine = create_engine('sqlite:///reviews.db')  
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add a new customer to the database
new_customer = Customer(first_name="John", last_name="Doe")
session.add(new_customer)
session.commit()

# Add a new restaurant to the database
new_restaurant = Restaurant(name="Sample Restaurant", price=3)
session.add(new_restaurant)
session.commit()

# Retrieve a customer and restaurant from the database
customer = session.query(Customer).first()
restaurant = session.query(Restaurant).first()

# Check if the customer and restaurant exist
if customer and restaurant:
    # Print information about the customer and restaurant
    print(f"Customer: {customer.full_name()}, Restaurants: {customer.restaurants()}")

    print(f"Restaurant: {restaurant.name}, Reviews: {restaurant.all_reviews()}")

    # Add a new review to the database
    new_review = Review(star_rating=5, customer=customer, restaurant=restaurant)
    session.add(new_review)
    session.commit()

    # Print all reviews for the restaurant
    print(f"All Reviews for {restaurant.name}: {restaurant.all_reviews()}")
else:
    print("No customer or restaurant found in the database.")
