# Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served,
# and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new numberand print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurant():
    """Modeling a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name, cuisine type attributes."""
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Give an explanation of the restaurant."""
        print(f'The restaurant is known as {self.restaurant_name.title()}.')
        print(f'It serves {self.cuisine_type}.')
        print(f'The restaurant has served {self.number_served} people so far. \n')

    def open_restaurant(self):
        """Show that the restaurant is open."""
        print(f'{self.restaurant_name.title()} is now open. Come get your {self.cuisine_type}. \n')

    def close_restaurant(self):
        """Show that the restaurant is close."""
        print(f'Sorry {self.restaurant_name.title()} is now closed. See you tomorrow. \n')

    def update_number_served(self, new_number):
        self.number_served = new_number

restaurant = Restaurant('maggies', 'chicken')
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
print(restaurant.update_number_served(60))
print(restaurant.describe_restaurant())
print(restaurant.close_restaurant())