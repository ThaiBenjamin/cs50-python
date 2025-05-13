import sys

def main():
    check_command_line()
    try:
        with open(sys.argv[1]) as file:
            reader = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    counter = 0
    for line in reader:
        if check_space_hashtag(line):
            counter += 1

    print(counter)

def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")

def check_space_hashtag(line):
    if line.isspace():
        return False
    if line.lstrip().startswith("#"):
        return False
    return True


if __name__ == "__main__":
    main()
