#Es 1 dictionaries notes

person = {
    "name": "Edgar",
    "age": 22,
    "job": "Maverick",
    "siblings": ["edwing","Irving"]

}

print(f"Name is {person["name"]}")
print(person.keys())
for key in person.keys():
    if key == "siblings":
        for name in person[key]:
            print(f"{person['name']} has a sibling named {name}")