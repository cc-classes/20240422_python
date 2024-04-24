from typing import TypedDict
import json


class HistoryEntryDict(TypedDict):
    id: int
    command: str
    operand: float


# high level
# implements the History contract
class HistoryDict:
    def __init__(self) -> None:
        # private
        self.__history: list[HistoryEntryDict] = []

    def get_history(self) -> list[tuple[int, str, float]]:
        entries: list[tuple[int, str, float]] = []
        for entry in self.__history:
            entries.append((entry["id"], entry["command"], entry["operand"]))
        return entries

    def next_entry_id(self) -> int:
        if self.__history:
            return max(entry["id"] for entry in self.__history) + 1
        return 1

    def append_history_entry(self, operation: str, operand: float) -> None:
        self.__history.append(
            {
                "id": self.next_entry_id(),
                "command": operation,
                "operand": operand,
            }
        )

    def remove_history_entry(self, entry_id: int) -> None:
        for entry in self.__history:
            if entry["id"] == entry_id:
                self.__history.remove(entry)
                break

    def clear_history_entries(self) -> None:
        self.__history.clear()

    def save_history(self) -> None:
        with open("history.json", "w") as file:
            json.dump(self.__history, file)

    def load_history(self) -> None:
        with open("history.json", "r") as file:
            self.__history = json.load(file)
