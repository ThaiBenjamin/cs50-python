import inflect
p=inflect.engine()
list_of_names = []

while True:

    try:
        user_input = input("Name: ")
        list_of_names.append(user_input)
    except EOFError:
        print("Adieu, adieu, to", p.join(list_of_names))
        break
