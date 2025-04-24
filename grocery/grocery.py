grocery_list = {}
while True:
    try:
        user_input = input("")
        if user_input not in grocery_list:
            grocery_list[user_input] = 1
        else:
            grocery_list[user_input] += 1
    except EOFError:
        break

for grocery in sorted(grocery_list):
    print(str(grocery_list[grocery]) + " " + grocery.upper())
