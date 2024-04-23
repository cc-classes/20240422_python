# from lib import add, subtract, PI
from featurea import lib  # import the lib module

from featurea.lib import add, subtract, PI  # import the functions and the variable

# bad approach, avoid it, never ever do this
# from lib import *


def main() -> None:
    result = lib.add(1, lib.subtract(3, 7))
    print(result)
    print(lib.PI)


if __name__ == "__main__":
    main()
