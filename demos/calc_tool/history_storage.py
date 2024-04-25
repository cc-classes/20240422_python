import json

from history import History


class HistoryStorage:
    def __init__(self, history: History) -> None:
        self.__history = history

    def save_history(self, file_name: str) -> None:
        with open(file_name, "w") as file:
            json.dump(list(self.__history), file)

    def load_history(self, file_name: str) -> None:
        with open(file_name, "r") as file:
            self.__history.bulk_import(json.load(file))
