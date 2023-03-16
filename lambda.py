people =[{"name": "Harry", "house": "Gryffindor"},
        {"name": "Cho", "house": "Ravenclaw"},
        {"name": "Draco", "house": "Slytherin"}
        ]
# the long way to order dict to dict
#def f(person):
#    return person["house"]

people.sort(key=lambda person: person["name"]) # the shortcut to do the same as the previous function

print(people)