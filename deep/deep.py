user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if ((user_input.lower() == "forty-two") or (user_input.lower() == "forty two") or ((user_input.strip()) == "42")):
    print("Yes")
else:
    print("No")
