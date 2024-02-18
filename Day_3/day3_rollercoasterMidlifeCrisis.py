print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
age = int(input("How old are you?\n"))
bill = 0

# if condition check mit ==, statt = 

if height > 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        bill = 5
        print("Child tickets are: $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are: $7")
    elif age < 45:
        bill = 12
        print("Adult tickets are: $12")
    elif age >= 45 and age <= 55:
        bill = 0

    wants_photo=input("Do you want a photo taken? Y or N.\n").upper()
    
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")