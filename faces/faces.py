def main():
    user_input = input("")
    new_emoji = convert(user_input)
    print(new_emoji)

def convert(message):
    message_happy_check = message.replace(":)", "🙂")
    message_final = message_happy_check.replace(":(", "🙁")
    return message_final

main()



