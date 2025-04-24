from pyfiglet import Figlet
import sys, random

figlet = Figlet()
figlet.getFonts()
figlet.setFont(font=f)
user_input = input("Input: ")
print("Output:",figlet.renderText(s))
