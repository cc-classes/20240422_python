from typing import Any


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
