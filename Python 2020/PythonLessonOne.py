#run with lists

#bicycles

bicycles = ["trek", "cannondale", "redline", "specialized"]

print(bicycles)


#access elements in a list
print(bicycles[0])
print(bicycles[1])


print(bicycles[-2])

#change, add and remove from this list

motorcycles = ["honda", "yamaha", "suzuki"]

print(motorcycles)

#changing
motorcycles[0] = "ducati"
print(motorcycles)

#adding
motorcycles.append("ducati")
print(motorcycles)

#insert
motorcycles.insert(0, "honda")
print(motorcycles)

#remove
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

#pop
popped_motorcycle = motorcycles.pop()
print(motorcycles)


#remove
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")

print(motorcycles)
motorcycles.remove("honda")
print(motorcycles)

#sorting
cars = ["bmw", "audi", "toyota", "subaru"]

#sorts temporary
print(sorted(cars))

#permanent sorting
cars.sort()
print(cars)


cars.sort(reverse=True)
print(cars)

#find the length of a list
print(len(cars))

#looping thru lists
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)

#number lists
for value in range(1,5):
    print(value)
    

#use range to make a list
numbers = list(range(1, 6))
print(numbers)

#even numbers list
even_numbers = list(range(2, 11, 2))
print(even_numbers)

million_numbers = list(range(1, 1_000_001))

print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

#slicing lists
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[1:4])
print(players[:4])

#copy a list
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[-2:]

print(my_foods)
print(friend_foods)
