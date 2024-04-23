from history import History

#low level: HistoryConsoleReporter -> History
class HistoryConsoleReporter:
    def __init__(self, history: History) -> None:
        self.history = history

    def print_history_entries(self) -> None:
        for entry in self.history.history:
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


class HistoryFileReporter:
    def __init__(self, history: History, file_name: str) -> None:
        self.history = history
        self.file_name = file_name

    def print_history_entries(self) -> None:
        with open(self.file_name, "w") as file:
            for entry in self.history.history:
                entry_id = entry.id
                entry_command = entry.command
                entry_operand = entry.operand
                file.write(
                    (
                        f"id: {entry_id}, "
                        f"command: {entry_command}, "
                        f"operand: {entry_operand}\n"
                    )
                )


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
