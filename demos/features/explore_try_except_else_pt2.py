def func() -> None:
    try:
        data = read_file("input.txt")
    except IOError:
        print("Error reading file")
        return

    try:
        processed_data = process_data(data)
    except ValueError:
        print("Error processing data")
        return

    try:
        write_file("output.txt", processed_data)
    except IOError:
        print("Error writing file")
        return
