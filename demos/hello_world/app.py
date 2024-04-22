def main() -> None:
    print(__name__)
    print("Hello, World!")


# why did we add this?
# file is a module, and a module is a file
# module - can be the executable or it can be a library
# executable: python ./app.py
# library: import app
# __name__ == "__main__" when the file is the executable
# use this guard, to only run code when it is the executable, otherwise, only
# the items in the module will be defined and available for import
if __name__ == "__main__":
    print("app")
    main()
