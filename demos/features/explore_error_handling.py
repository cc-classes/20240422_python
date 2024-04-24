import logging

logging.basicConfig(level=logging.INFO)


class CalcAppDivideByZeroError(Exception): ...


def divide(x: float, y: float) -> float:
    if y == 0:
        raise CalcAppDivideByZeroError("Calc app cannot divide by zero")
    return x / y


def main() -> None:
    try:
        result = divide(1, 0)
        print(result)
    except CalcAppDivideByZeroError as e:
        logging.error(f"Calc App Divide By Zero Error: {e}")
    # more general purpose error to catch anything unexpected
    except Exception as e:
        logging.error(f"General Purpose Error: {e}")


if __name__ == "__main__":
    main()
