class HistoryEntry:
    def __init__(self, entry_id: int, operation: str, operand: float) -> None:
        self.id = entry_id
        self.command = operation
        self.operand = operand

    def __str__(self) -> str:
        return f"{self.id}: {self.command} {self.operand}"


# high level
# implements the History contract
class HistoryObj:
    def __init__(self) -> None:
        self.__history: list[HistoryEntry] = []

    def get_history(self) -> list[tuple[int, str, float]]:
        entries: list[tuple[int, str, float]] = []
        for entry in self.__history:
            entries.append((entry.id, entry.command, entry.operand))
        return entries

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
