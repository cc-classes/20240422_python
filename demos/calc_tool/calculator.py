from typing import Any, Callable

calc_fns: dict[str, Callable[[float, float], float]] = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y,
}


def calculator_result(history: list[dict[str, Any]]) -> float:
    result = 0.0
    for entry in history:
        command = entry["command"]
        operand = entry["operand"]
        calc_fn = calc_fns[command]
        result = calc_fn(result, operand)
    return result
