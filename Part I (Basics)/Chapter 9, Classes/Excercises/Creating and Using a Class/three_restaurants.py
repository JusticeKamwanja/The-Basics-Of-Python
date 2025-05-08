# Start with your class from Exercise 9-1.
# Create three different instances from the class,
# and call describe_restaurant() for each instance.

class Restaurant():
    """Modeling a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name, cuisine type attributes."""
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Give an explanation of the restaurant."""
        print(f'\nThe restaurant is known as {self.restaurant_name.title()}.')
        print(f'It serves {self.cuisine_type}.')

    def open_restaurant(self):
        """Show that the restaurant is open."""
        print(f'\n{self.restaurant_name.title()} is now open. Come get your {self.cuisine_type}.')

    def close_restaurant(self):
        """Show that the restaurant is close."""
        print(f'\nSorry {self.restaurant_name.title()} is now closed. See you tomorrow.')

my_hotel = Restaurant('maggies', 'chicken')
pearls_hotel = Restaurant('the pearl', 'fish')
moms_hotel = Restaurant('ceejays', 'fries')

pearls_hotel.describe_restaurant()
my_hotel.describe_restaurant()
moms_hotel.describe_restaurant()