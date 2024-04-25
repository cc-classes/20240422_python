from typing import TypedDict
import json

from history import HistoryIterator


class HistoryEntryDict(TypedDict):
    id: int
    command: str
    operand: float


class HistoryDictIterator:
    def __init__(self, history_entries: list[HistoryEntryDict]) -> None:
        self.__history_entries = history_entries
        self.__index = 0

    def __next__(self) -> tuple[int, str, float]:
        if self.__index < len(self.__history_entries):
            entry = self.__history_entries[self.__index]
            self.__index += 1
            return (entry["id"], entry["command"], entry["operand"])
        raise StopIteration


# high level
# implements the History contract
class HistoryDict:
    def __init__(self) -> None:
        # private
        self.__history: list[HistoryEntryDict] = []

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

    # def save_history(self) -> None:
    #     with open("history.json", "w") as file:
    #         json.dump(self.__history, file)

    # def load_history(self) -> None:
    #     with open("history.json", "r") as file:
    #         self.__history = json.load(file)

    def bulk_import(
        self, history_entries: list[tuple[int, str, float]]
    ) -> None:
        self.__history = [
            {"id": entry[0], "command": entry[1], "operand": entry[2]}
            for entry in history_entries
        ]

    def __iter__(self) -> HistoryIterator:
        return HistoryDictIterator(self.__history)
