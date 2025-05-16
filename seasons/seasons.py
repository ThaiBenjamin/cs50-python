from datetime import datetime, date
import inflect
import sys

class AgeInMinutes:
    def __init__(self, birth_date_str):
        try:
            self.birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date")

    def calculate_minutes(self):
        today = date.today()
        delta = today - self.birth_date
        return round(delta.total_seconds() / 60)

    def to_words(self):
        minutes = self.calculate_minutes()
        p = inflect.engine()
        return p.number_to_words(minutes, andword="").capitalize() + " minutes"

def minutes_to_words(birth_date_str):
    age = AgeInMinutes(birth_date_str)
    return age.to_words()

def main():
    user_input = input("Birth date: ")
    try:
        print(minutes_to_words(user_input))
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
