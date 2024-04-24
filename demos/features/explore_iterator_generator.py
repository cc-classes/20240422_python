def my_range(num):
    counter = 0
    while counter < num:
        print("in the while loop")
        # the yield makes it a generator
        yield counter
        print("returned to make your dreams come true!")
        counter += 1


for num in my_range(5):
    print("in the for loop")
    print(num)
