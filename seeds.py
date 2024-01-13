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
print("Restaurant added successfully!")

# Add customers
customer1 = Customer(first_name="Alice", last_name="Johnson")
customer2 = Customer(first_name="Bob", last_name="Smith")
customer3 = Customer(first_name="Charlie", last_name="Brown")

session.add_all([customer1, customer2, customer3])
session.commit()
print("Customer added successfully!")

# Add reviews
review1 = Review(star_rating=5, customer=customer1, restaurant=restaurant1)
review2 = Review(star_rating=4, customer=customer2, restaurant=restaurant1)
review3 = Review(star_rating=3, customer=customer1, restaurant=restaurant2)
review4 = Review(star_rating=5, customer=customer3, restaurant=restaurant3)

session.add_all([review1, review2, review3, review4])
session.commit()

print("Review added successfully!")

customer = session.query(Customer).first()
restaurant = session.query(Restaurant).first()

# Print initial reviews for the customer
print("Initial reviews for the customer:")
for review in customer.reviews:
    print(review.full_review())

# Delete all reviews for the given restaurant
customer.delete_reviews(session, restaurant)

# Print remaining reviews for the customer (after deletion)
print("Remaining reviews for the customer:")
for review in customer.reviews:
    print(review.full_review())

session.commit()
session.close()
