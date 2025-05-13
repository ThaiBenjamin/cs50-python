import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    user_input = ip
    return re.search(r".+[0-255]/..+[0-255]/..+[0-255]/..+[0-255]", user_input)

if __name__ == "__main__":
    main()
