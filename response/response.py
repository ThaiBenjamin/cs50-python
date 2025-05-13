from validator_collection import validators, checkers

user_input = input("What's your email address? ")

try:
    if checkers.is_email(user_input, allow_empty = False):
        print("Valid")
    else:
        print("Invalid")
except:
    print("Invalid")


