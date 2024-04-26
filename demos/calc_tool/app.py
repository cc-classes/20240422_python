import logging
from datetime import datetime

from user_input import get_command
from user_output import (
    HistoryConsoleReporter,
    HistoryFileReporter,
    print_invalid_command,
    print_result,
)
from calculator import calculator_result, calc_fns
from history_obj import HistoryObj
from history_dict import HistoryDict
from history import History
from history_storage import get_history_storage
from app_settings import AppSettings


def create_history_factory(kind: str = "obj") -> History:
    if kind == "dict":
        return HistoryDict()
    return HistoryObj()


class InvalidCommandFormatError(Exception): ...


def parse_command(command: str) -> tuple[str, str | None]:
    import re

    command_without_args_pattern = re.compile(r"^[a-z]+$")
    command_with_args_pattern = re.compile(r"^([a-z]+) (\S+)$")

    command_with_args_match = command_with_args_pattern.match(command)

    if command_with_args_match:
        return command_with_args_match.groups()
    elif command_without_args_pattern.match(command):
        return (command, None)
    else:
        raise InvalidCommandFormatError(command)


class CalculatorTool:
    def __init__(self, app_settings: AppSettings, history: History):
        self.__app_settings = app_settings
        self.__history = history

    def display_result(self) -> None:
        try:
            print_result(calculator_result(self.__history))
        except ZeroDivisionError as e:
            logging.error(e)
            print(
                (
                    "Unable to display result, error in history of "
                    "operations, please clear or remove before proceeding,"
                )
            )

    def command_calculation(self, command_name: str, command_arg: str) -> None:
        try:
            operand = float(command_arg)
            if command_name == "divide" and operand == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            self.__history.append_history_entry(command_name, operand)
            self.display_result()
        except ValueError as e:
            logging.error(e)
            print(f"Invalid math operand: {command_arg}")
        except ZeroDivisionError as e:
            logging.error(e)
            print("Invalid division by zero")

    def run(self) -> None:
        logging.log(logging.INFO, "app started")
        while True:
            try:
                command_name, command_arg = parse_command(get_command())

                with open(
                    self.__app_settings.command_log_file, "a"
                ) as command_log_file:
                    command_log_file.write(
                        (
                            f"timestamp: {datetime.now().isoformat()}"
                            f", command: {command_name}, args: {command_arg}\n"
                        )
                    )

            except InvalidCommandFormatError as e:
                logging.error(e)
                print("Invalid command format")
                continue

            if command_name in calc_fns:
                self.command_calculation(command_name, command_arg)
            elif command_name == "history":
                HistoryConsoleReporter(self.__history).print_history_entries()
                HistoryFileReporter(
                    self.__history, "entries.txt"
                ).print_history_entries()
            elif command_name == "remove":
                # add error handling
                self.__history.remove_history_entry(int(command_arg))
            elif command_name == "save":
                if not command_arg:
                    command_arg = "history.json"
                get_history_storage(command_arg, self.__history).save_history(
                    command_arg
                )
            elif command_name == "load":
                if not command_arg:
                    command_arg = "history.json"
                get_history_storage(command_arg, self.__history).load_history(
                    command_arg
                )
            elif command_name == "clear":
                self.__history.clear_history_entries()
            elif command_name == "exit":
                return
            else:
                print_invalid_command(command_name)
                logging.warning(f"Invalid command: {command_name}")


def main() -> None:
    # builder pattern which is being done with the chain pattern
    app_settings = (
        AppSettings()
        .command_line_args()
        .load_app_configuration()
        .configure_logging()
    )
    history = create_history_factory("obj")
    calculator_tool = CalculatorTool(app_settings, history)
    calculator_tool.run()


if __name__ == "__main__":
    main()
