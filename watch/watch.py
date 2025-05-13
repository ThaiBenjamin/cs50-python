import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search("^(https?://(?:www\.)?youtube.com)/embed/(.+))",s)
    if match:
        return match.group(1) + match.group(2)
    else:
        return None




if __name__ == "__main__":
    main()
