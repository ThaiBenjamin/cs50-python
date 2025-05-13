import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    user_input = ip

    if match := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", user_input):
        if match.group(1) and math.group(2)
    else:
        return False

if __name__ == "__main__":
    main()
