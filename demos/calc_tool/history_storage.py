import json

from history import History


class HistoryStorage:
    def __init__(self, history: History) -> None:
        self.__history = history

    def save_history(self) -> None:
        with open("history.json", "w") as file:
            json.dump(list(self.__history), file)

    def load_history(self) -> None:
        with open("history.json", "r") as file:
            self.__history.bulk_import(json.load(file))
