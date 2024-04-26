from typing import Any


class App:
    def __init__(self) -> None:
        self.__routes = {}

    def route(self, path: str) -> callable:
        def wrapper(fn: callable) -> callable:
            self.__routes[path] = fn

            # def inner(*args, **kwargs):
            #     print(f"never executes - path: {path}")
            #     return fn(*args, **kwargs)

            # return inner

        return wrapper

    def run(self, path: str, *args, **kwargs) -> Any:
        fn = self.__routes[path]
        return fn(*args, **kwargs)


app = App()


@app.route("/add")
def add(a: int, b: int) -> int:
    return a + b


print(app.run("/add", 2, 3))
