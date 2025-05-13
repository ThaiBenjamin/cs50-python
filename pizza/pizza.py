import csv
import sys
from tabulate import tabulate

def main():
    check_command_line()
    print(tabulate(read(sys.argv[1]), headers="keys", tablefmt="grid") )



def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


def read(name):
    if name == "regular.csv":
        with open("regular.csv") as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                students.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
            return students

    elif name == "sicilian.csv":
        with open("sicilian.csv") as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                students.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})
            return students
    else:
        sys.exit("CSV file does not exist")


if __name__ == "__main__":
    main()
