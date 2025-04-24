import inflect
while True:

    list_of_names = []
    try:
        user_input = input("Name: ")
        list_of_names.append(user_input)
    except EOFError:
        print("Adieu, adieu, to", inflect.join(list_of_names))
