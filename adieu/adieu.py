import inflect
p=inflect.engine()
list_of_names = []

while True:
    user_input = input("Name: ")
    try:
        list_of_names.append(user_input)
    except EOFError:
        print("Adieu, adieu, to", p.join(list_of_names))
