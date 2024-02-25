import random

longName = "Angela, Ben, Jenny, Michael, Chloe"
names = longName.split(", ")
nameLength = len(names)

randomPicker = random.randint(0, nameLength-1)
chosenOne = names[randomPicker]

print(f"{chosenOne} is going to by the meal today!")

