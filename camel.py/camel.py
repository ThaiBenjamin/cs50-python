user_input = input("camelCase: ")
new_string = ""
for c in user_input:
    if c.islower():
        new_string += c
    else:
        new_string += "_" + c.lower()



print("snake_case:",new_string)
