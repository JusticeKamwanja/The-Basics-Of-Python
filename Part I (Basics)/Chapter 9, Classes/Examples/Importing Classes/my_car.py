from car_module import Car
from electric_car_module import ElectricCar


my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


new_car = Car('audi', 'a4', 2016)
print(new_car.get_descriptive_name())

new_car.set_odometer_reading = 60 + 10
new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()