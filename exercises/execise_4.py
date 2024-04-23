from typing import Any

def input_str(prompt: str) -> str:
    return input(prompt)

def input_float(prompt: str) -> float:
    return float(input_str(prompt))

def input_int(prompt: str) -> int:
    return int(input_str(prompt))

def get_command() -> str:
    return input_str("Enter a command: ")

def get_operand() -> float:
    return input_float("Enter operand: ")

def get_entry_id() -> int:
    return input_int("Enter entry id: ")

def next_entry_id(history: list[dict[str, Any]]) -> int:
    if history:
        return max(entry["id"] for entry in history) + 1
    return 1

def append_history_entry(
    operation: str, operand: float, history: list[dict[str, Any]]
) -> None:
    history.append(
        {
            "id": next_entry_id(history),
            "command": operation,
            "operand": operand,
        }
    )

def clear_history_entries(history: list[dict[str, Any]]) -> None:
    history.clear()

def main() -> None:
    result = 0.0
    history: list[dict[str, Any]] = []
    history_id = 0

    while True:
        command = get_command()

        if command == "add":
            operand = get_operand()
            result = result + operand
            history_id += 1
            append_history_entry("add", operand, history)
        elif command == "subtract":
            operand = get_operand()
            result = result - operand
            history_id += 1
            append_history_entry("subtract", operand, history)
        elif command == "multiply":
            operand = get_operand()
            result = result * operand
            history_id += 1
            append_history_entry("multiply", operand, history)
        elif command == "divide":
            operand =  get_operand()
            result = result / operand
            history_id += 1
            append_history_entry("divide", operand, history)
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
            clear_history_entries(history)
        elif command == "exit":
            return
        else:
            print(f"Invalid command: {command}")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    main()