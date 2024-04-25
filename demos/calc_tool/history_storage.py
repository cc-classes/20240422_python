import json
from typing import Protocol
import csv
from pathlib import Path

from history import History


class HistoryStorage(Protocol):
    def save_history(self, file_name: str) -> None: ...

    def load_history(self, file_name: str) -> None: ...


def get_history_storage(file_name: str, history: History) -> HistoryStorage:
    if file_name.endswith(".json"):
        return HistoryJsonStorage(history)
    elif file_name.endswith(".csv"):
        return HistoryCsvStorage(history)
    else:
        raise ValueError(f"not a valid file extension: {file_name}")


class HistoryJsonStorage:
    def __init__(self, history: History) -> None:
        self.__history = history

    def save_history(self, file_name: str) -> None:
        with open(file_name, "w") as file:
            json.dump(list(self.__history), file)

    def load_history(self, file_name: str) -> None:
        with open(file_name, "r") as file:
            self.__history.bulk_import(json.load(file))


class HistoryCsvStorage:
    def __init__(self, history: History) -> None:
        self.__history = history

    def save_history(self, file_name: str) -> None:
        history_file_path = Path(file_name)
        with history_file_path.open("w", encoding="UTF-8") as history_file:
            history_csv_writer = csv.writer(history_file, delimiter=",")
            for entry in self.__history:
                history_csv_writer.writerow(entry)

    def load_history(self, file_name: str) -> None:
        history_file_path = Path(file_name)
        with history_file_path.open("r", encoding="UTF-8") as history_file:
            history_csv_reader = csv.reader(history_file, delimiter=",")
            self.__history.bulk_import(list(history_csv_reader))
