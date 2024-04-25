import json

from history import HistoryIterator


class HistoryEntry:
    def __init__(self, entry_id: int, operation: str, operand: float) -> None:
        self.id = entry_id
        self.command = operation
        self.operand = operand

    def __str__(self) -> str:
        return f"{self.id}: {self.command} {self.operand}"


class HistoryObjIterator:
    def __init__(self, history_entries: list[HistoryEntry]) -> None:
        self.__history_entries = history_entries
        self.__index = 0

    def __next__(self) -> tuple[int, str, float]:
        if self.__index < len(self.__history_entries):
            entry = self.__history_entries[self.__index]
            self.__index += 1
            return (entry.id, entry.command, entry.operand)
        raise StopIteration


# high level
# implements the History contract
class HistoryObj:
    def __init__(self) -> None:
        self.__history: list[HistoryEntry] = []

    def next_entry_id(self) -> int:
        if self.__history:
            return max(entry.id for entry in self.__history) + 1
        return 1

    def append_history_entry(self, operation: str, operand: float) -> None:
        self.__history.append(
            HistoryEntry(self.next_entry_id(), operation, operand)
        )

    def remove_history_entry(self, entry_id: int) -> None:
        for entry in self.__history:
            if entry.id == entry_id:
                self.__history.remove(entry)
                break

    def clear_history_entries(self) -> None:
        self.__history.clear()

    # def save_history(self) -> None:
    #     with open("history.json", "w") as file:
    #         json.dump(
    #             [
    #                 {
    #                     "id": entry.id,
    #                     "command": entry.command,
    #                     "operand": entry.operand,
    #                 }
    #                 for entry in self.__history
    #             ],
    #             file,
    #         )

    # def load_history(self) -> None:
    #     with open("history.json", "r") as file:
    #         history = json.load(file)
    #         self.__history = [
    #             HistoryEntry(entry["id"], entry["command"], entry["operand"])
    #             for entry in history
    #         ]

    def bulk_import(
        self, history_entries: list[tuple[int, str, float]]
    ) -> None:
        self.__history = [
            HistoryEntry(entry[0], entry[1], entry[2])
            for entry in history_entries
        ]

    def __iter__(self) -> HistoryIterator:
        return HistoryObjIterator(self.__history)
