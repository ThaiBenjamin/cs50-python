from pyfiglet import Figlet

user_input = input("Input: ")
f = Figlet(font=get)
print("Output:",f.renderText(user_input))
