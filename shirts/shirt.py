import sys
from PIL import Image, ImageOps

def main():
    check_command_line()
    new_shirt()

def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Image does not exist")
    if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) or not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")
    if sys.argv[1].lower().endswith(".jpg") != sys.argv[2].lower().endswith(".jpg") or sys.argv[1].lower().endswith(".jpeg") != sys.argv[2].lower().endswith(".jpeg") or sys.argv[1].lower().endswith(".png") != sys.argv[2].lower().endswith(".png"):
        sys.exit("Input and output have different extensions")


def new_shirt():
    user = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(user, size)
    muppet.paste(shirt, shirt)

    muppet.save(sys.argv[2])


if __name__ == "__main__":
    main()
