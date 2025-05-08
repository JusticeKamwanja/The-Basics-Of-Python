class Car():
    """An attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes describing a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f'The car is a {self.year} {self.make.title()} {self.model.title()}.'
        return long_name
    
    def read_odometer(self):
        """Show the car's mileage."""
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll back the odometer reading"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        
        else:
            print("ERROR!! You can't roll back an odometer!!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("ERROR!! You cannot roll back an odometer!!")
        
        elif miles >= 0:
            self.odometer_reading += miles
    
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
print(my_used_car.read_odometer())

my_used_car.update_odometer(1000)
print(my_used_car.get_descriptive_name())
print(my_used_car.read_odometer())

my_used_car.update_odometer(1200)

print(my_used_car.get_descriptive_name())
print(my_used_car.read_odometer())

my_used_car.increment_odometer(500)

print(my_used_car.get_descriptive_name())
print(my_used_car.read_odometer())

my_used_car.increment_odometer(-1000)

print(my_used_car.get_descriptive_name())
print(my_used_car.read_odometer())