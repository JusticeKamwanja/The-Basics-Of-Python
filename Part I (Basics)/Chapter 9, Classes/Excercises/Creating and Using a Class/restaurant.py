# Make a class called Restaurant.

# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.

# Make a method called describe_restaurant() that prints these two pieces of information,

# and a method called open_restaurant() that prints a message indicating that the restaurant is open.

# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant():
    """Modeling a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name, cuisine type attributes."""
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Give an explanation of the restaurant."""
        print(f'The restaurant is known as {self.restaurant_name.title()}.')
        print(f'It serves {self.cuisine_type}.')

    def open_restaurant(self):
        """Show that the restaurant is open."""
        print(f'{self.restaurant_name.title()} is now open. Come get your {self.cuisine_type}.')

    def close_restaurant(self):
        """Show that the restaurant is close."""
        print(f'Sorry {self.restaurant_name.title()} is now closed. See you tomorrow.')

my_hotel = Restaurant('maggies', 'chicken')
my_hotel.describe_restaurant()
my_hotel.open_restaurant()