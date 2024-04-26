from typing import Callable


def wrapper(fn: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("inside of inner")
        return fn(*args, **kwargs)

    return inner


@wrapper
def do_it(a, b) -> int:
    return a + b


# wrapped_do_it = wrapper(do_it)
# print(wrapped_do_it(1, 2))

print(do_it(1, 2))


