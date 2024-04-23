def main() -> None:
    total: int | float = 1 + 2
    print(total)

    total = 1 + total
    print(total)

    total = 1 + 2 * 3
    print(total)

    total = (1 + 2) * 3
    print(total)

    total = 1 + 2 / 3
    print(total)


if __name__ == "__main__":
    main()
