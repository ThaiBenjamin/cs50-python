import random


while True:
    try:
        upper_bound = int(input("Level: "))
        if(upper_bound > 0):
            break
        else:
            continue
    except ValueError:
        continue


guessing_number = random.randint(1, upper_bound)

current_guess = None

while current_guess != guessing_number:

    while True:
        try:
            current_guess = int(input("Guess: "))
            break
        except ValueError:
            continue

    if current_guess == guessing_number:
        print("Just right!")


    elif current_guess > guessing_number:
        print("Too large!")



    else:
        print("Too small!")



