# a car class

class Car:

    """A simple attempt to represent a car."""

    #object constructor
    def __init__(self, make, model, year):

        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        #default attribute
        self.odometer_reading = 0

    #methods
    def get_descriptive_name(self):

        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):

        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, miles):

        self.odometer_reading += miles

    def fill_gas_tank(self):

        print("Filled tank")
