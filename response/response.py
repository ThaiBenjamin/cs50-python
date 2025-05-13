from validator_collection import validators

user_input = input("What's your email address? ")

print(validators.email(user_input, allow_empty = False))
