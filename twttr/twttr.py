user_input = input("Input: ")
output = ""

for c in user_input:
    if c.lower() == "a" or c.lower() == "e" or c.lower() == "i" or c.lower() == "o" or c.lower() == "u":
        continue
    else:
        output += c

print("Output:",output)
