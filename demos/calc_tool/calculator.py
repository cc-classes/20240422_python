from typing import Callable

from history import History

calc_fns: dict[str, Callable[[float, float], float]] = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y,
}


def calculator_result(history: History) -> float:
    result = 0.0
    for entry in history.get_history():
        command = entry[1]
        operand = entry[2]
        calc_fn = calc_fns[command]
        result = calc_fn(result, operand)
    return result
