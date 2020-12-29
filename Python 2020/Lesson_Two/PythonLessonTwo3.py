#object oriented programming with classes

from PythonLessonTwo2 import Dog
from PythonLessonTwo4 import Car
from PythonLessonThreeAliens import Electric_Car
#create a dog

my_dog = Dog("willie", 6)

#info on my dog
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

#make my dog do tricks
my_dog.sit()
my_dog.roll_over()

#make another dog
your_dog = Dog("Lucy", 3)

#info on my dog 
print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")

#make my dog do tricks
your_dog.sit()
your_dog.roll_over()

#create a new car
my_new_car = Car("Audi", "a4", 2019)

print(my_new_car.get_descriptive_name())

#use default attribute
my_new_car.read_odometer()

#went on a test drive
my_new_car.odometer_reading = 23

my_new_car.read_odometer()

#went to taco bell
my_new_car.update_odometer(13)

my_new_car.read_odometer()

my_new_car.fill_gas_tank()

#inheritance or create a child class
my_tesla = ElectricCar("tesla", "roadster", "2020")

my_tesla.describe_battery()
