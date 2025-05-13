import csv
import sys

def main():
    check_command_line()
    convert_students_csv()

def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Could not read " + sys.argv[1])
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

def convert_students_csv():
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        with open(sys.argv[2], "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames =["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(",")
                last = last.strip()
                first = first.strip()
                writer.writerow({"first": first, "last": last, "house":row["house"]})





if __name__ == "__main__":
    main()

