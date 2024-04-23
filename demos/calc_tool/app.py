from typing import Any
from user_input import get_command, get_operand, get_entry_id
from user_output import (
    print_history_entries,
    print_invalid_command,
    print_result,
    print_error,
)
from calculator import calculator_result, calc_fns
from history import (
    append_history_entry,
    remove_history_entry,
    clear_history_entries,
)


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
