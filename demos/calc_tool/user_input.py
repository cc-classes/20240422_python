def input_str(prompt: str) -> str:
    return input(prompt + " > ")


def input_float(prompt: str) -> float:
    return float(input_str(prompt))


def input_int(prompt: str) -> int:
    return int(input_str(prompt))


def get_command() -> str:
    return input_str("Enter a command")


def get_operand() -> float:
    return input_float("Enter operand")


def get_entry_id() -> int:
    return input_int("Enter entry id")
