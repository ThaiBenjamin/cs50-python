fruit = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantalopue": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit":90,
    "lemon":15,
    "lime":20,
    "nectarine":60,
    "orange":80,
    "peach":60,
    "pear":100,
    "pineapple":50,
    "plums":70,
    "strawberries":50,
    "sweet cherries":100,
    "tangerine":50,
    "watermelon":80,
}

user_input = input("Item: ")

if user_input.lower() in fruit:
    print("Calories:",fruit[user_input.lower()])
