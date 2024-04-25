from pathlib import Path
import csv


def write_csv() -> None:
    names_file_path = Path("names.csv")
    with names_file_path.open("w", encoding="UTF-8") as names_file:
        names_csv_writer = csv.writer(names_file, delimiter=",")
        names_csv_writer.writerow(["first_name", "last_name"])
        names_csv_writer.writerow(["Bob", "Smith"])
        names_csv_writer.writerow(["Alice", "Springs"])
        names_csv_writer.writerow(["Jim", "Timmons"])
        names_csv_writer.writerow(["Sally", "Wakefield"])


def read_csv() -> None:
    names_file_path = Path("names.csv")
    with names_file_path.open("r", encoding="UTF-8") as names_file:
        names_csv_reader = csv.reader(names_file, delimiter=",")

        # skip the header row
        next(names_csv_reader)

        # only print out the data
        for name_row in names_csv_reader:
            print(name_row)


def write_csv_dict() -> None:
    names_file_path = Path("names.csv")
    field_names = ["first_name", "last_name"]
    with names_file_path.open("w", encoding="UTF-8") as names_file:
        names_csv_writer = csv.DictWriter(
            names_file, fieldnames=field_names, delimiter="\t"
        )

        names_csv_writer.writeheader()

        names_csv_writer.writerow({"first_name": "Bob", "last_name": "Smith"})
        names_csv_writer.writerow(
            {"first_name": "Alice", "last_name": "Springs"}
        )
        names_csv_writer.writerow(
            {"first_name": "Jim", "last_name": "Timmons"}
        )
        names_csv_writer.writerow(
            {"first_name": "Sally", "last_name": "Wakefield"}
        )


def read_csv_dict() -> None:
    names_file_path = Path("names.csv")
    with names_file_path.open("r", encoding="UTF-8") as names_file:
        names_csv_reader = csv.DictReader(names_file, delimiter="\t")

        for names_row in names_csv_reader:
            print(names_row)


def main() -> None:
    # write_csv()
    # read_csv()
    # write_csv_dict()
    read_csv_dict()


if __name__ == "__main__":
    main()
