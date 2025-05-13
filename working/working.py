import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"([0-9_: ]+(?:AM)?(?:PM)?) to ([0-9_: ]+(?:AM)?(?:PM)+)",s):
        first_number = match.group(1)
        first_number_components= re.split(r"[: ]", first_number)
        second_number = match.group(2)
        second_number_components= re.split(r"[: ]", second_number)

        converted_first_hours = 0
        converted_second_hours = 0

        if first_number_components[2] == "PM":
            converted_first_hours = int(first_number_components[0]) + 12

        else:
            

        if second_number_components[2] == "PM":
            converted_second_hours = int(second_number_components[0]) + 12


        print(str(converted_first_hours) + str(converted_second_hours))



        print(first_number_components)




    else:
        raise ValueError


if __name__ == "__main__":
    main()
