import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"(https?://www\.youtube\.com)/embed/([a-zA-Z0-9_]+)",s)
    if match:
        return match.group(1) + match.group(2)
    else:
        return None




if __name__ == "__main__":
    main()
