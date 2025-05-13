import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",s):
        list = match.groups()
    else:
        raise ValueError

    first_hours = int(list[1])
    first_minutes = list[2]
    second_hours = int(list[5])
    second_minutes = list[6]

    if list[3] == "PM":
        first_hours = 12 + first_hours
    else:
        first_hours = 0 + first_hours

    if list[7] == "PM":
        second_hours = 12 + second_hours
    else:
        second_hours = 0 + second_hours

    if first_minutes == None:
        first_minutes = "00"


    if second_minutes == None:
        second_minutes = "00"
    

    if len(str(first_hours)) == 1:
        first_hours = "0"+ str(first_hours)
    if len(str(second_hours)) == 1:
        second_hours = "0"+ str(second_hours)

    return (f"{first_hours}:{first_minutes} to {second_hours}:{second_minutes}")

if __name__ == "__main__":
    main()
