class HistoryEntry:
    def __init__(self, entry_id: int, operation: str, operand: float) -> None:
        self.id = entry_id
        self.command = operation
        self.operand = operand

    def __str__(self) -> str:
        return f"{self.id}: {self.command} {self.operand}"


class History:
    def __init__(self) -> None:
        self.history: list[HistoryEntry] = []

    def next_entry_id(self) -> int:
        if self.history:
            return max(entry.id for entry in self.history) + 1
        return 1

    def append_history_entry(self, operation: str, operand: float) -> None:
        self.history.append(
            HistoryEntry(self.next_entry_id(), operation, operand)
        )

    def remove_history_entry(self, entry_id: int) -> None:
        for entry in self.history:
            if entry.id == entry_id:
                self.history.remove(entry)
                break

    def clear_history_entries(self) -> None:
        self.history.clear()
