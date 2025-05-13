def main():
    user_input = input("Input: ")
    print("Output:", shorten(user_input))

def shorten(n):

    output = ""
    for c in n:
        if c.lower() == "a" or c.lower() == "e" or c.lower() == "i" or c.lower() == "o" or c.lower() == "u":
            continue
        else:
            output += c
    return output

if __name__ == "__main__":
    main()
