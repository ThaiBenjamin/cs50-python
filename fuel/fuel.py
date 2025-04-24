while True:
    user_input = input("Fraction: ").split("/")

    try:
        new_num = int(user_input[0])/int(user_input[1])
        if new_num <= 0.01:
            print("E")
            break
        elif new_num >= 0.99 and new_num <= 1:
            print("F")
            break
        elif new_num > 1:
            raise ValueError
        else:
            print(str(round(new_num*100)) + "%")
            break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
