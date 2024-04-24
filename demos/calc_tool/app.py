import logging

from user_input import get_command, get_operand, get_entry_id
from user_output import (
    HistoryConsoleReporter,
    HistoryFileReporter,
    print_invalid_command,
    print_result,
    print_error,
)
from calculator import calculator_result, calc_fns
from history_obj import HistoryObj
from history_dict import HistoryDict
from history import History


def create_history_factory(kind: str = "obj") -> History:
    if kind == "dict":
        return HistoryDict()
    return HistoryObj()


class CalculatorTool:
    def __init__(self, history: History):
        self.history = history

    def run(self) -> None:
        while True:
            command = get_command()

            if command in calc_fns:
                try:
                    operand = get_operand()
                    if command == "divide" and operand == 0:
                        raise ZeroDivisionError("Cannot divide by zero")
                    self.history.append_history_entry(command, operand)
                except ZeroDivisionError as e:
                    logging.error(e)
                    continue
            elif command == "history":
                HistoryConsoleReporter(self.history).print_history_entries()
                HistoryFileReporter(
                    self.history, "entries.txt"
                ).print_history_entries()
            elif command == "remove":
                self.history.remove_history_entry(get_entry_id())
            elif command == "clear":
                self.history.clear_history_entries()
            elif command == "exit":
                return
            else:
                print_invalid_command(command)
                logging.warning(f"Invalid command: {command}")
                continue

            try:
                print_result(calculator_result(self.history))
            except ZeroDivisionError as e:
                logging.error(e)
                print(
                    (
                        "Unable to display result, error in history of "
                        "operations, please clear or remove before proceeding,"
                    )
                )


def main() -> None:
    history = create_history_factory("obj")
    calculator_tool = CalculatorTool(history)
    calculator_tool.run()


if __name__ == "__main__":
    main()
