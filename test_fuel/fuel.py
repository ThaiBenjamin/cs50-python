def main():
    user_input = input("Fraction: ")
    print(gauge(convert(user_input)))



def convert(fraction):
    while True:
        try:
            slash_position = fraction.find("/")
            num = int(fraction[0:slash_position])
            num2 = int(fraction[slash_position+1:])

            if num/num2 <= 1:
                return round(num/num2 * 100)

            else:
                fraction = input("Fraction: ")
                pass
        except ZeroDivisionError:
            raise
        except ValueError:
            raise

def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return ("F")
    else:
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()


