
def num_input(prompt: str) -> int:
    return int(input(prompt))

def sum_nums(a: int, b: int) -> int:
    return a + b

def main() -> None:
    num1 = num_input("Enter a number: ")
    num2 = num_input("Enter another number: ")

    # break this out into a function to divide responsibilities
    print(f"Sum: {sum_nums(num1, num2)}")

if __name__ == "__main__":
    main() 