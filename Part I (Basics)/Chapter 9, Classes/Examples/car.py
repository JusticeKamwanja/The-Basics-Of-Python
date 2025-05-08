class Car():
    """An attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes describing a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def __repr__(self) -> str:
        return 'This is a car class.'
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f'{self.year} {self.make} {self.model}.'
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
        self.odometer_reading += miles
    
gari = Car('audi', 'a4', 2016)
print(repr(gari))