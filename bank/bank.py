user_input = input("Greeting: ")
if(user_input.lower().strip()[0:5] == "hello"):
    print("$0")
elif(user_input.lower().strip()[0] == "h"):
    print("$20")
else:
    print("$100")
