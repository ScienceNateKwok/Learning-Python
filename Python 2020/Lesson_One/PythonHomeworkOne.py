#Question One

people = ["Mom", "Dad", "Sister"]

for person in people:
    print("Hi there, " + person + ", you are invited to dinner!")

#Question Two

for person in people:
    print("Hi there, " + person + ", I have found a bigger table so I can invite more people!")

people.insert(0, "Grandmother")
people.insert(2, "Bob")
people.append("Joe")

for person in people:
    print("Hi there, " + person + ", you are invited to dinner!")

#Question Three (Functions)

def display_message():
    print("May I have your attention please, I am learning about how to code in Python!")

display_message()

#Question Four (Functions)

def favorite_book(title):
    return"One of my favorite books is " + title

favorite = favorite_book("'Wolf Hallow'.")

print(favorite)

#Question Five (Dictionaries)

favorite_numbers = {
                        "Nathan":42,
                        "Arsheel":69,
                        "Jackson":11,
                        "Ryan":100,
                        "Charlie":100000
                    }
for name, number in favorite_numbers.items():
    print(f"Name: {name}\tNumber: {number}")

#Question Six (Dictionaries)

print(favorite_numbers)
