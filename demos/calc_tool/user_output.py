from history import HistoryEntry


def print_history_entries(history: list[HistoryEntry]) -> None:
    for entry in history:
        entry_id = entry.id
        entry_command = entry.command
        entry_operand = entry.operand
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
