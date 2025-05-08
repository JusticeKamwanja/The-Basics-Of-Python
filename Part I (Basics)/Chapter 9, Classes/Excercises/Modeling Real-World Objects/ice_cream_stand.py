# An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171).
# Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.


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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        self.flavours = ['chocolate', 'strawberry', 'butterscotch', 'mint', 'oreo', 'mango']

    def show_flavours(self):
        print(f'At {self.restaurant_name.title()}, we offer {self.cuisine_type.lower()} with the following flavours:')
        flavour_number = 0
        
        for flavour in self.flavours:
            flavour_number +=1
            output = f'{flavour_number}. {flavour.title()}.'
            print(output)

        print('\n')



my_stand = IceCreamStand('kamwanja ice', 'Ice Cream')
your_stand = IceCreamStand('ice ice', 'Ice Cream')

your_stand.show_flavours()
my_stand.show_flavours()
your_stand.show_flavours()