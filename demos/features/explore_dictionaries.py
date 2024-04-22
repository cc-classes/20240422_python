from typing import Any

# creating a dictionary object and assigning to the person variable
person: dict[str, Any] = {"first_name": "Bob", "last_name": "Smith", "age": 23}

# printing the current key-value pairs
print(person["first_name"])
print(person["last_name"])
print(person["age"])

# print the whole dictionary
print(person)

# update the existing key-value pair
person["age"] = 24

# add a new key-value pair
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
except Exception as e:
    print("Exception: ", e)

# safely access a key that may not exist, and
# use a default value if the key is not found
print(person.get("middle_name", "N/A"))

# remove a key-value pair
del person["hair_color"]

# the dictionary object will now be garbage collected
# person = None


for num in range(10):
    person = {}

    person["num"] = num