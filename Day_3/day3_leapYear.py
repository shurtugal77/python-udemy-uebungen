# Check current year
currentYear = int(input("What year do you want to check?\n"))

yearModulo4 = currentYear % 4
yearModulo100 = currentYear % 100
yearModulo400 = currentYear % 400

if yearModulo4 == 0:
    if yearModulo100 == 0:
        if yearModulo400 == 0:
            print(f"The year {currentYear} is a leap year.")
        else:
            print(f"The year {currentYear} is not a leap year.")
    else:
        print(f"The year {currentYear} is a leap year.")
            
else:
    print(f"The year {currentYear} is not a leap year.")