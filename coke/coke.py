amount = 50
while amount > 0:
    print("Amount Due:",str(amount))
    user_input = input("Insert Coin: ")
    if user_input == "25" or user_input == "10" or user_input == "5":
        amount -= int(user_input)
    else:
        continue


print("Change Owed:", str((amount*-1)))
