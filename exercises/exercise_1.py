def main() -> None:
    result = 0

    while True:
        # caputure user input from command line
        command = input("Enter a command: ")

        if command == "clear":
            # reset result to 0
            result = 0
            print(f"Result: {result}")
            
        elif command == "exit":
            # will exit the loop
            break

        elif command == "add":
            operand = float(input("Please enter an operand: "))
            # add result
            result += operand
            print(f"Result: {result}")

        elif command == "subtract":
            operand = float(input("Please enter an operand: "))
            result += operand
            print(f"Result: {result}")

        elif command == "multiply":
            operand = float(input("Please enter an operand: "))
            result += operand
            print(f"Result: {result}")

        elif command == "divide":
            operand = float(input("Please enter an operand: "))
            result += operand
            print(f"Result: {result}")

        else:
            print(f"Invalid command: {command}")


if __name__ == "__main__":
    main()