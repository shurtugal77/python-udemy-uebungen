# BMI Calculator 2.0
yourWeight = float(input("Wie viel wiegst du in [kg]?\n"))
yourHeight = float(input("Wie groß bist du in [cm]?\n"))
yourHeightMeter = yourHeight/100

BMI = yourWeight / yourHeightMeter**2
floatBMI = round(BMI, 1)
intBMI = int(BMI)
print(f"Dein BMI ist {BMI} bzw. gerundet {intBMI}")


if floatBMI < 18.5:
    print("You are underweight")
elif floatBMI < 25:
    print("You are normal weight")
elif floatBMI < 30:
    print("You are slightly overweight")
elif floatBMI <= 35:
    print("You are obese")
else:
    print("You are clinically obese")
