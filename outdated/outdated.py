month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user_input = input("Date: ").strip()
    try:
        month, day, year = user_input.split("/")
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            print(f"{year}-{int(month):02}-{int(day):02}")
        else:
            continue
    except ValueError:
        try:
            month, day, year = user_input.split(' ')
            if month in month_list and 1 <= int(day[0]) <= 31 and ',' in day:
                if day[0:2].isdigit():
                    if int(day[0:2]) <= 31:
                        print(f"{year}-{month_list.index(month)+1:02}-{int(day[0:2]):02}")
                    else:
                        continue
                else:
                    print(f"{year}-{month_list.index(month)+1:02}-{int(day[0]):02}")
            else:
                continue
        except ValueError:
            continue

    break

