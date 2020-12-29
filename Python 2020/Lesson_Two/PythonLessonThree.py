# an electric car class

from PythonLessonTwo4 import Car
class Electrical_Car (Car):

    """Represents electric car, inherits everything from car class"""

    def __init__(self, make, model, year):

        """pass these values to the parent class"""
        super().__init__(make, model, year)

        """now initalize unique attributes of the child class"""
        self.battery_size = 100

    #methods
    def describe_battery(self):

        """print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):

        """override orginal fill function"""
        print(f"This car does not take gasoline as a fuel source.")
