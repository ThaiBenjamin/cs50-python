import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"([0-9_: ]+(?:AM)?(?:PM)?) to ([0-9_: ]+(?:AM)?(?:PM)+)",s):
        first_number_components = match.group(1).split(":")
        second_number_components = match.group(2).split(":")

        print(first_number_components)




    else:
        raise ValueError


if __name__ == "__main__":
    main()
