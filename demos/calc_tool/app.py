from typing import Any, Callable

calc_fns: dict[str, Callable[[float, float], float]] = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y,
}


def input_str(prompt: str) -> str:
    return input(prompt + " > ")


def input_float(prompt: str) -> float:
    return float(input_str(prompt))


def input_int(prompt: str) -> int:
    return int(input_str(prompt))


def get_command() -> str:
    return input_str("Enter a command")


def get_operand() -> float:
    return input_float("Enter operand")


def get_entry_id() -> int:
    return input_int("Enter entry id")


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


def remove_history_entry(entry_id: int, history: list[dict[str, Any]]) -> None:
    for entry in history:
        if entry["id"] == entry_id:
            history.remove(entry)
            break


def clear_history_entries(history: list[dict[str, Any]]) -> None:
    history.clear()


def print_history_entries(history: list[dict[str, Any]]) -> None:
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


def print_invalid_command(command: str) -> None:
    print(f"Invalid command: {command}")


def print_result(result: float) -> None:
    print(f"Result: {result}")


def print_error(message: str) -> None:
    print(f"Error: {message}")


def calculator_result(history: list[dict[str, Any]]) -> float:
    result = 0.0
    for entry in history:
        command = entry["command"]
        operand = entry["operand"]
        calc_fn = calc_fns[command]
        result = calc_fn(result, operand)
    return result


def main() -> None:
    history: list[dict[str, Any]] = []

    while True:
        command = get_command()

        if command in calc_fns:
            operand = get_operand()
            if command == "divide" and operand == 0:
                print_error("Cannot divide by zero")
                continue
            append_history_entry(command, operand, history)
        elif command == "history":
            print_history_entries(history)
        elif command == "remove":
            remove_history_entry(get_entry_id(), history)
        elif command == "clear":
            clear_history_entries(history)
        elif command == "exit":
            return
        else:
            print_invalid_command(command)
            continue

        print_result(calculator_result(history))


if __name__ == "__main__":
    main()
