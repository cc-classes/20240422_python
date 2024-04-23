person = {
    "first_name": "Bob",
    "last_name": "Smith",
    "age": 23,
}

print(person["first_name"])
print(person["last_name"])
print(person["age"])

print(person)

person["age"] = 24
person["hair_color"] = "brown"

# first_name Bob
# last_name Smith
# age 24
# hair_color brown

for key in person:
    print(key, person[key])

# try to access a key that does not exist, you will get a KeyError
try:
    print(person["middle_name"])
except KeyError:
    print("KeyError: middle_name")

# safely access a key that may not exist, and
# use default value if key is not found
print(person.get("middle_name", "N/A"))
