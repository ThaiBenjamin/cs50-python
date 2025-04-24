from pyfiglet import Figlet

user_input = input("Input: ")
f = Figlet()
print("Output:",f.renderText(user_input))
