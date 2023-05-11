def read_file():
    with open('event.ics', 'r') as reader:
        # Read & print the entire file
        print(reader.read())