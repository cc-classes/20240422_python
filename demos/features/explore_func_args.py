# x and y are parameters
# a parameter is a variable declaration and assignment
def add(x, y):


    return x + y


# 1 and 2 are arguments
# an argument is an expression that is evaluate, and the result of the
# evaluation is passed into the function
result = add(1, 2)
print(result)


num1 = 4
result2 = add(num1, 2)
print(result)

result2 = add(num1 + 1, 2)
print(result)