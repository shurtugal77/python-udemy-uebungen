# BMI Calculator
yourWeight = float(input("Wie viel wiegst du in [kg]?\n"))
yourHeight = float(input("Wie groß bist du in [cm]?\n"))
yourHeightMeter = yourHeight/100

BMI = yourWeight / yourHeightMeter**2

intBMI = int(BMI)

print(f"Dein BMI ist {BMI} bzw. gerundet {intBMI}")