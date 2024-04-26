try:
    data = read_file("input.txt")
except IOError:
    print("Error reading file")
else:
    try:
        processed_data = process_data(data)
    except ValueError:
        print("Error processing data")
    else:
        try:
            write_file("output.txt", processed_data)
        except IOError:
            print("Error writing file")
finally:
    print("cover everything")
