#revising dictionaries

#alien
alien0 = {
            "color":"green",
            "points":5
         }

print(f"You just hit {alien0['color']} alien")
print(f"you earned {alien0['points']} points")

#add new key value pair
alien0["xpos"] = 0
alien0["ypos"] = 25
alien0["speed"] = "slow"

print(alien0)

#change values of keys in dictionary
alien0["color"] = "yellow"
print(alien0)

#remove a key value pair in dictionary
del alien0["points"]
print(alien0)

#dictionary of similar objects
favorite_languages = {
                        "jen":"python",
                        "sarah":"c",
                        "edward":"ruby on rails",
                        "phil":"python"
                    }


#what is sarah's fav programming languagef
print(favorite_languages["sarah"])

#what if I don't know if a key exists
#get() if you don't know a key exists
points = alien0.get("points", "point key not found")
print(points)

#loop thru the dictionary
user0 = {
            "username":"efermi",
            "first":"enrico",
            "last":"fermi"
        }
for key, value in user0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")


for name, language in favorite_languages.items():
    print(name + "---" + language)

for name in favorite_languages.keys():
    print(name)

for language in favorite_languages.values():
    print(language)



alien0 = {
            "color":"green",
            "points":5
         }
alien1 = {
            "color":"yellow",
            "points":10
         }
alien2 = {
            "color":"red",
            "points":15
         }

#list of aliens
aliens = [alien0, alien1, alien2]

print(aliens)


for alien in aliens:
    print(alien)

#example
#make an empty list for sorting aliens
aliens = []

#make 30 green aliens
for alien_number in range(1,31):
    new_alien = {
                    "color":"green",
                    "points":5
                }
    aliens.append(new_alien)

#show the first 5 aliens
    for alien in aliens[0:5]:
        print(alien)

print(len(aliens))

#a list in a dictionary

pizza = {
            "crust":"pan",
            "toppings":["mushrooms", "extra cheese"]
        }

print(pizza)

for topping in pizza["toppings"]:
    print(topping)

#dictionary in a dictionary

users = {
            "aeinstein":{
                            "first":"albert",
                            "lasts":"einstein",
                            "location":"princeton"
                        },
            "mcurie":{
                        "first":"marie",
                        "last":"curie",
                        "location":"paris"
                    }
        }
for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    print(f"\nUserinfo: {userinfo}")
