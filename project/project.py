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
    current_guess = input("Guess a number between " + str(lower_bound) + " and " + str(upper_bound) + ": " ))
    check_guess(current_guess, guessing_number)

    while check_guess_correctness(current_guess, guessing_number) == False:
        while check_guess(current_guess, guessing_number) != True:
            current_guess = input("Guess a number between " + str(lower_bound) + " and " + str(upper_bound) + ": " ))
        counter+=1

    print(guessing_number)


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

def guess_number(guess, random_number)
counter = 0
current_guess = None

def check_guess(user_guess):
    try:
        current_guess = int(user_guess)
    except ValueError:
        print("Please input a valid integer")
        return False


def check_guess_correctness(user_guess, random_generated_number)
    if current_guess != random_generated_number:
        return False

    if current_guess == guessing_number:
        return True

        print("The number was " + str(guessing_number) + ", you got it correct!")
        counter += 1
        if counter <= math.floor(math.log(upper_bound-lower_bound+1, 2)):
            if counter > 1:
                print("Congrats you win it took you " + str(counter) + " attempts!")
            else:
                print("Congrats you win it took you 1 attempt!")
        else:
            if math.floor(math.log(upper_bound-lower_bound+1, 2)) > 1:
                print("You suck loser it took you more then " + str(math.floor(math.log(upper_bound-lower_bound+1, 2))) + " tries!")
                print("It took you " + str(counter) + " attempts!")
            else:
                print("You suck loser it took you more then 1 try!")

    elif current_guess < guessing_number:
        print("Guess a number that's higher")
        counter += 1



    else:
        print("Guess a number that's lower")
        counter += 1

if __name__ == "__main__":
     main()

"""
