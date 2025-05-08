from random import choice

class Car():
    """An attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes describing a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel_amount = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        full_car_name = f'{self.year} {self.make} {self.model}.'
        message = f'The car is a {full_car_name} \n'
        return message
    
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

    def fill_gas_tank(self, fuel_amount):
        self.fuel_amount = fuel_amount
    
    def check_gas_tank(self):
        """Check the fuel amount"""
        if self.fuel_amount == 40:
            print(f'Your fuel tank is full.')

        elif self.fuel_amount > 10:
            print(f'Your tank is {self.fuel_amount} litres full.')
            
        elif 1 <= self.fuel_amount <= 10:
            print(choice([
                    (f'Your fuel tank is almost empty, fill up.'),
                    (f'You are running out of fuel!!'),
                ]))
        
        elif self.fuel_amount == 0:
            print("You're out of fuel!!. Fill up your tank!!")

        elif self.fuel_amount > 40:

            print(f'Your tank can only hold 40 litres!!')

class ElectricCar(Car):
    """Represent aspect of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize atttributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f'The car has a {self.battery_size}-kWh battery. \n')

    def fill_gas_tank(self):
        """Gas? LOL. emojize(:laughing_face:)"""
        print("It's an EV, so it does not need a gas tank. \n")


my_ev = ElectricCar('tesla', 'model s', 2016)
print(my_ev.get_descriptive_name())
my_ev.describe_battery()
my_ev.fill_gas_tank()

# my_car = Car('toyota', 'vitz', 2018)
# my_car.fill_gas_tank(40)
# my_car.check_gas_tank()
# my_car.fill_gas_tank(10+30)
# my_car.check_gas_tank()
# my_car.fill_gas_tank(32)
# my_car.check_gas_tank()
# my_car.fill_gas_tank(10)
# my_car.check_gas_tank()
# my_car.fill_gas_tank(8)
# my_car.check_gas_tank()
# my_car.fill_gas_tank(0)
# my_car.check_gas_tank()
