def main() -> None:
    # infinite loop
    while True:
        # capture user input from the command line
        command = input("Enter a command: ")

        if command == "exit":
            # break will exit the loop
            break

        # echo the command to the command line
        # f-string is a convenient way to format strings (string interpolation)
        print(f"Received command: {command}")


if __name__ == "__main__":
    main()
