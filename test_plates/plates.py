def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s.isalpha():
            return True
        elif s.isalnum() and s[0:2].isalpha():
            for c in s:
                if c.isdigit():
                    index = s.index(c)

                    if s[index:].isdigit() and c != "0":
                        return True

                    else:
                        return False


if __name__ == "__main__":
    main()
