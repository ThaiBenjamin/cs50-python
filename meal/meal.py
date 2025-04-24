def main():
    user_input = input("What time is it? ")


    new_time = convert(user_input)

    if 7 <= new_time <= 8:
        print("breakfast time")
    elif 12 <= new_time <= 13:
        print("lunch time")
    elif 18 <= new_time <= 20:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    if minutes.strip()[-4:] == "A.M.":
        new_minutes = minutes.replace(" A.M.","")
        return (float(hours) + float(new_minutes)/60)
    if minutes.strip()[-4:] == "P.M.":
        new_minutes = minutes.replace(" P.M.","")
        return (float(hours)+12 + float(new_minutes)/60)

    return (float(hours) + float(minutes)/60)


if __name__ == "__main__":
    main()
