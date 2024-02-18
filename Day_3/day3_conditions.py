print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
age = int(input("How old are you?\n"))

# if condition check mit ==, statt = 

if height > 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        print("Your price is: $5")
    elif age <=18:
        print("Your price is: $7")
    else:
        print("Your price is: $12")
else:
    print("Sorry, you have to grow taller before you can ride.")