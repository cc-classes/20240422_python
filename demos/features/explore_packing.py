# item = (1, "Bob", "red", "green", "blue")

# # unpacking
# # * is the packing operator
# id, name, *colors = item

# print(id)
# print(name)
# print(colors)

# # * is the unpacking operator
# new_colors = ["black", *colors, "purple"]
# print(new_colors)

# # * is the packing operator = * is the unpacking operator
# # variable = expression

# # params = variables
# # args = expression


# # * - packing
# def my_func(*args):
#     print("hello")


# # * - unpacking
# my_func(*["a", 1, True])


# # x = 1
# # y = 2
# def add(x, y):
#     return x + y


# add(1, 2)


person = {"name": "Bob", "age": 23}

person2 = {**person, "city": "Boston"}

print(person2)
