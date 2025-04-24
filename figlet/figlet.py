from pyfiglet import Figlet
import sys, random

figlet = Figlet()
fonts = figlet.getFonts()
f = ""
if len sys.argv == 1:
    f=random.choice(fonts)
elif len sys.argv == 3:
figlet.setFont(font=f)
user_input = input("Input: ")
print("Output:",figlet.renderText(s))


