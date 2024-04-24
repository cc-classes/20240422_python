# module scope
my_var = "hello, world!"


def func1():
    # use the variable from the outer scope

    # am I using a new variable or the existing?
    my_var = "you all are the best!"

    print(f"func1: {my_var}")  # func1: hello, world!

    def func2():
        nonlocal my_var

        my_var = "mapping the world and beyond is awesome!"

        print(f"func2: {my_var}")  # func2: hello, world!

    func2()

    print(f"func1: {my_var}")  # func1: hello, world!


func1()

print(f"module: {my_var}")  # module: hello, world!
