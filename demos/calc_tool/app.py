from typing import Any


def main() -> None:
    result = 0.0
    history: list[dict[str, Any]] = []
    history_id = 0

    while True:
        command = input("Enter a command: ")

        if command == "add":
            operand = float(input("Enter operand: "))
            result = result + operand
            history_id += 1
            history.append(
                {"id": history_id, "command": command, "operand": operand}
            )
        elif command == "subtract":
            operand = float(input("Enter operand: "))
            result = result - operand
            history_id += 1
            history.append(
                {"id": history_id, "command": command, "operand": operand}
            )
        elif command == "multiply":
            operand = float(input("Enter operand: "))
            result = result * operand
            history_id += 1
            history.append(
                {"id": history_id, "command": command, "operand": operand}
            )
        elif command == "divide":
            operand = float(input("Enter operand: "))
            result = result / operand
            history_id += 1
            history.append(
                {"id": history_id, "command": command, "operand": operand}
            )
        elif command == "history":
            for entry in history:
                entry_id = entry["id"]
                entry_command = entry["command"]
                entry_operand = entry["operand"]
                print(
                    (
                        f"id: {entry_id}, "
                        f"command: {entry_command}, "
                        f"operand: {entry_operand}"
                    )
                )
        elif command == "remove":
            entry_id = int(input("Enter entry id: "))
            for entry in history:
                if entry["id"] == entry_id:
                    history.remove(entry)
                    break
        elif command == "clear":
            result = 0.0
            history.clear()
        elif command == "exit":
            return
        else:
            print(f"Invalid command: {command}")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    main()
