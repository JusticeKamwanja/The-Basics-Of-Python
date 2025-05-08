from car_module import Car

"""A set of classes used to represent electric cars."""

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f'The car has a {self.battery_size}-kWh battery. \n')

    def get_range(self):
        """Print a statement about the range this abttery provides."""
        if self.battery_size == 70:
            range = 240

        if self.battery_size == 85:
            range = 270


        message = f'This car can go approximately {range}'
        message += ' miles on a full charge. \n'
        print(message)

class ElectricCar(Car):
    """Represent aspect of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize atttributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f'The car has a {self.battery_size}-kWh battery. \n')

    def fill_gas_tank(self):
        """Gas? LOL. emojize(:laughing_face:)"""
        print("It's an EV, so it does not need a gas tank. \n")
