# main.py

from customer import Customer
from restaurant import Restaurant
from review import Review

# Create customers
customer1 = Customer("John", "Doe")
customer2 = Customer("Alice", "Smith")

# Create restaurants
restaurant1 = Restaurant("Burger King")
restaurant2 = Restaurant("Pizza Hut")

# Add reviews
customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant1, 5)
customer2.add_review(restaurant2, 3)

# Test methods
print(customer1.full_name())  # Output: John Doe
print(restaurant1.average_star_rating())  # Output: 4.5
print(customer2.num_reviews())  # Output: 2
print(Customer.find_by_name("John Doe"))  # Output: <Customer object>
print(Customer.find_all_by_given_name("Alice"))  # Output: [<Customer object>]
