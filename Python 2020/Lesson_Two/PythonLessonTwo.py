#learning about functions

import PythonLessonTwoExtra
from PythonLessonTwoExtra import make_pizza as mp
##########START FUNCTIONS HERE###############

def greet_user(username):
    print(f"\n Hello {username}")

def describe_pet(animal_type, pet_name):
    print("\nI have an animal of type " + animal_type)
    print("My pet's name is " + pet_name)

def describe_pet(animal_type, pet_name="cuddle"):
    print("\nI have an animal of type " + animal_type)
    print("My pet's name is " + pet_name)

def get_formatted_name(first, last):
    full_name = first + " " + last
    return full_name

def person_dictionary(first, last, age=None):
    person = {
                "first":first,
                "last":last,
             }
    if age:
        person["age"] = age

    return person

def greet_users(names):
    for name in names:
        msg = f"Hello {name.title()}"
        print(msg)

def make_pizza(*toppings):
    print(toppings)
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

def build_profile(first, last, **user_info):
    print(user_info)
    user_info["first"] = first
    user_info["last"] = last
    return user_info

###########END FUNCTIONS HERE###############

#arguments and parameters
greet_user("jesse")

describe_pet("hamster", "harry")

#order matters
describe_pet("harry", "hamster")


#use keywords to match parameter list if unordered
describe_pet(pet_name="harry", animal_type="hamster")

#default values
describe_pet("hamster")

#return values
musician = get_formatted_name("justin", "beiber")
print(musician)

#return a dictionary
person0 = person_dictionary("jimmy", "hendrix")
person1 = person_dictionary("jimmy", "hendrix", age=27)

print(person0)
print(person1)

#pass a list
usernames = ["hannah", "ty", "margot"]
greet_users(usernames)

#passing an arbitrary number of arguments
make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

#arbitrary keyword arguments
user_profile = build_profile("albert", "einstien", location="princeton", field="physics")
print(user_profile)

#store functions modules
PythonLessonTwoExtra.make_pizza(16, "pepperoni")
PythonLessonTwoExtra.make_pizza(12, "mushrooms", "green peppers", "extra cheese")


#giving functions alias
mp(7, "jalapenos")
