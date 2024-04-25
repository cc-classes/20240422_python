from pathlib import Path
import yaml


def write_colors() -> None:
    try:
        colors = ["red", "green", "blue"]
        colors_file_path = Path("colors.txt")

        with colors_file_path.open("w", encoding="UTF-8") as colors_file:
            for color in colors:
                colors_file.write(f"{color}\n")

    except IOError as exc:
        print(f"Error: {exc}")


def read_colors() -> None:
    try:
        colors = []
        colors_file_path = Path("colors.txt")

        with colors_file_path.open("r", encoding="UTF-8") as colors_file:
            for color in colors_file:
                colors.append(color.strip())

        print(colors)

    except IOError as exc:
        print(f"Error: {exc}")


def write_person() -> None:
    try:
        person = {
            "first_name": "Bob",
            "last_name": "Smith",
            "address": {"city": "Boston", "state": "MA"},
            "phone_numbers": ["123-123-1234", "234-234-2345"],
        }

        person_file_path = Path("person.yml")

        with person_file_path.open("w", encoding="UTF-8") as person_file:
            person_yaml = yaml.dump(person)
            person_file.write(person_yaml)

    except IOError as exc:
        print(f"Error: {exc}")


def read_person() -> None:
    try:
        person_file_path = Path("person.yml")

        with person_file_path.open("r", encoding="UTF-8") as person_file:
            person = yaml.load(person_file, Loader=yaml.SafeLoader)
            print(person)

    except IOError as exc:
        print(f"Error: {exc}")


def main() -> None:
    # write_colors()
    # read_colors()
    # write_person()
    read_person()


if __name__ == "__main__":
    main()
