def main() -> None:
    result = 0.0

    while True:
        command = input("Enter a command: ")

        if command == "add":
            operand = float(input("Enter operand: "))
            result = result + operand
        elif command == "subtract":
            operand = float(input("Enter operand: "))
            result = result - operand
        elif command == "multiply":
            operand = float(input("Enter operand: "))
            result = result * operand
        elif command == "divide":
            operand = float(input("Enter operand: "))
            result = result / operand
        elif command == "clear":
            result = 0.0
        elif command == "exit":
            return
        else:
            print(f"Invalid command: {command}")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    main()
