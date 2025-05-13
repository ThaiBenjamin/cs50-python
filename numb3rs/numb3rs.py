import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    user_input = ip

    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", user_input):
        number_list = user_input.split(".")
        for i in number_list:
            if int(i) < 0 or int(i) > 255:
                return False
        return True
    else:
        return False
if __name__ == "__main__":
    main()
