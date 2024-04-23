from typing import Protocol

# History Protocol
from history import History

class HistoryReporter(Protocol):
    def print_history_entries(self) -> None:
        ...


# low level: HistoryConsoleReporter -> History
class HistoryConsoleReporter:
    def __init__(self, history: History) -> None:
        self.history = history

    def print_history_entries(self) -> None:
        for entry in self.history.get_history():
            print(
                (
                    f"id: {entry[0]} "
                    f"operation: {entry[1]} "
                    f"operand: {entry[2]}"
                )
            )


class HistoryFileReporter:
    def __init__(self, history: History, file_name: str) -> None:
        self.history = history
        self.file_name = file_name

    def print_history_entries(self) -> None:
        with open(self.file_name, "w") as file:
            for entry in self.history.get_history():
                file.write(
                    (
                        f"id: {entry[0]} "
                        f"operation: {entry[1]} "
                        f"operand: {entry[2]}"
                    )
                )


def print_invalid_command(command: str) -> None:
    print(f"Invalid command: {command}")


def print_result(result: float) -> None:
    print(f"Result: {result}")


def print_error(message: str) -> None:
    print(f"Error: {message}")
