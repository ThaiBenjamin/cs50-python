import random
import math



def main():
    print("Welcome to Ben's Guessing Dooms Game!")
    print("You will have a certain number of guesses to guess your number from a range of your choosing!")
    lower_bound = input("What is your lower bound: ")
    upper_bound = input("What is your upper bound: ")
    if check_bounds(lower_bound, upper_bound):
        generate_random_number(lower_bound, upper_bound)


def check_bounds(lower, upper):
    while True:
        try:
            lower_bound = int(lower)
            upper_bound = int(upper)
            break
        except ValueError:
            print("Please print a valid integer")

    while lower_bound >= upper_bound:
            print("Make sure your lower bound is smaller than your upper bound")
            while True:
                try:
                    lower_bound = int(input("What is your lower bound: "))
                    upper_bound = int(input("What is your upper bound: "))
                    break
                except ValueError:
                    print("Please input a valid integer")
    return True

def generate_random_number(lower, upper):



guessing_number = random.randint(lower_bound, upper_bound)

counter = 0
current_guess = None

while current_guess != guessing_number:

    while True:
        try:
            current_guess = int(input("Guess a number between " + str(lower_bound) + " and " + str(upper_bound) + ": " ))
            break
        except ValueError:
            print("Please input a valid integer")

    if current_guess == guessing_number:
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



