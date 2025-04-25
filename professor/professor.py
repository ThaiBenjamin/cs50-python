import random


def main():
    level = get_level()

    counter = 0
    score = 0
    incorrect_counter = 0
    while counter < 10:
        if incorrect_counter == 0:
            integer1 = generate_integer(level)
            integer2 = generate_integer(level)
        print(str(integer1) + " + " + str(integer2) + " = ", end = "")
        user_input = input("")


        if user_input == str(integer1+integer2):
            counter += 1
            score += 1
            incorrect_counter = 0
            continue

        else:
            print("EEE")
            incorrect_counter +=1
            if incorrect_counter == 3:
                print((str(integer1) + " + " + str(integer2)) + " = " + str(integer1+integer2))
                incorrect_counter = 0
                counter += 1
                continue

    print("Score:", str(score))


def get_level():

    while True:
        try:
            user_input = int(input("Level: "))
            if user_input != 1 and user_input != 2 and user_input != 3:
                continue
            else:
                return user_input

        except ValueError:
            continue




def generate_integer(level):
    if level != 1 and level != 2 and level != 3:
        raise ValueError
    else:
        if level == 1:
            return random.randint(0,9)
        elif level == 2:
            return random.randint(10,99)
        elif level == 3:
            return random.randint(100,999)




if __name__ == "__main__":
    main()
