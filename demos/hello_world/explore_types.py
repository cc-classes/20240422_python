from typing import Any


def main() -> None:
    some_var: Any = "Hello, World!"

    print(type(some_var))

    some_var = 42

    print(type(some_var))


if __name__ == "__main__":
    main()
