import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    user_input = ip

    if match := re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", user_input):
        number_list = user_input.split(".")
        for i in number_list:
            if int(i) >= 0 and int(i) <= 255:
                continue
            else:
                return False
        return True
    return False
if __name__ == "__main__":
    main()
