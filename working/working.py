import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"([0-9_: ]+(?:AM)?(?:PM)?) to ([0-9_: ]+(?:AM)?(?:PM)+)",s):
        first_number = match.group(1).strip()
        second_number = match.group(2).strip()

        if "PM" in first_number:
            first_number = first_number.remove("PM")
            print(first_number)
        if "PM" in second_number:
            second_number = second_number.remove("AM")
            print(second_number)

    else:
        raise ValueError


if __name__ == "__main__":
    main()
