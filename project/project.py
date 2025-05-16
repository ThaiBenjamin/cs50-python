import random
import math



def main():
    print("Welcome to Ben's Guessing Dooms Game!")
    print("You will have a certain number of guesses to guess your number from a range of your choosing!")
    lower_bound = input("What is your lower bound: ")
    upper_bound = input("What is your upper bound: ")

    while check_bounds(lower_bound, upper_bound) == False:
        lower_bound = input("What is your lower bound: ")
        upper_bound = input("What is your upper bound: ")

    lower_bound = int(lower_bound)
    upper_bound = int(upper_bound)

    guessing_number = generate_random_number(lower_bound, upper_bound)

    counter = 1
    current_guess = input("Guess a number between " + str(lower_bound) + " and " + str(upper_bound) + ": " )

    while check_guess(current_guess) == False:
            current_guess = input("Guess a number between " + str(lower_bound) + " and " + str(upper_bound) + ": " )
            give_hint(current_guess, guessing_number)

    current_guess = int(current_guess)

    while check_guess_correctness(current_guess, guessing_number) == False:
        current_guess = input("Guess a number between " + str(lower_bound) + " and " + str(upper_bound) + ": " )
        while check_guess(current_guess) == False:
            current_guess = input("Guess a number between " + str(lower_bound) + " and " + str(upper_bound) + ": " )
        current_guess = int(current_guess)
        counter+=1
        print(counter)
        give_hint(current_guess, guessing_number)

    victory_decider(counter, guessing_number, lower_bound, upper_bound)



def check_bounds(lower, upper):
    try:
        lower_bound = int(lower)
        upper_bound = int(upper)
    except ValueError:
        print("Please use valid integer(s)")
        return False

    if lower_bound >= upper_bound:
            print("Make sure your lower bound is smaller than your upper bound")
            return False

    return True

def generate_random_number(lower, upper):
    guessing_number = random.randint(lower, upper)
    return guessing_number


def check_guess(user_guess):
    try:
        int(user_guess)
    except ValueError:
        print("Please input a valid integer")
        return False
    return True


def check_guess_correctness(user_guess, random_generated_number):
    if user_guess != random_generated_number:
        return False

    if user_guess == random_generated_number:
        return True

def give_hint(user_guess, random_generated_number):
    if user_guess > random_generated_number:
        print("Guess a number that's lower")

    else:
        print("Guess a number that's higher")


def victory_decider(counter, random_generated_number, lower_bound, upper_bound):
    print("The number was " + str(random_generated_number) + ", you got it correct!")
    if counter <= math.floor(math.log(upper_bound-lower_bound+1, 2)):
        if counter > 1:
            print("Congrats you win it took you " + str(counter) + " attempts!")
        else:
            print("Congrats you win it took you 1 attempt!")
    else:
        if math.floor(math.log(upper_bound-lower_bound+1, 2)) > 1:
            print("You lost took you more then " + str(math.floor(math.log(upper_bound-lower_bound+1, 2))) + " tries!")
            print("It took you " + str(counter) + " attempts!")
        else:
            print("You lost it took you more then 1 try!")

if __name__ == "__main__":
     main()


