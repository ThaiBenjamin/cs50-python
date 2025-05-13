import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        match = re.search(r"(https?://(?:www\.)?youtu)(be\.com/)embed/([a-z_A-Z_0-9]+)",s)
        if match:
            return match.group(1) + "." + match.group(2) + match.group(3)
    else:
        return None




if __name__ == "__main__":
    main()
