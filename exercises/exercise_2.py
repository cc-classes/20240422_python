from typing import Any

def main() -> None:
    result = 0
    history: list[dict[str, Any]] = []
    history_id = 0

    while True:
        # caputure user input from command line
        command = input("Enter a command: ")

        if command == "clear":
            # reset result to 0
            result = 0
            history.append({"id": history_id, "command": command, "operand": operand})
        elif command == "exit":
            # will exit the loop
            break

        elif command == "add":
            operand = float(input("Please enter an operand: "))
            # add result
            result = result + operand
            history.append({"id": history_id, "command": command, "operand": operand})

        elif command == "subtract":
            operand = float(input("Please enter an operand: "))
            result = result - operand
            history.append({"id": history_id, "command": command, "operand": operand})

        elif command == "multiply":
            operand = float(input("Please enter an operand: "))
            result = result * operand
            history.append({"id": history_id, "command": command, "operand": operand})

        elif command == "divide":
            operand = float(input("Please enter an operand: "))
            result = result / operand
            history.append({"id": history_id, "command": command, "operand": operand})

        elif command == "history":
            for entry in history:
                print(entry)

        else:
            print(f"Invalid command: {command}")


if __name__ == "__main__":
    main()