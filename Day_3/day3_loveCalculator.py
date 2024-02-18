print("The Love Calculator is calculating your score")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

trueCalc = "0"
loveCalc = "0"

# Oder mit einem Zähler für "LOVE" und "TRUE"

countT = 0
countR = 0
countU = 0
countE = 0
countL = 0
countO = 0
countV = 0

combinedNameString = (name1 + name2).lower()

countT += combinedNameString.count("t")
countR += combinedNameString.count("r")
countU += combinedNameString.count("u")
countE += combinedNameString.count("e")
countL += combinedNameString.count("l")
countO += combinedNameString.count("o")
countV += combinedNameString.count("v")

trueCalc = countT + countR + countU + countE
loveCalc = countL + countO + countV + countE

lovePercent = str(trueCalc) + str(loveCalc)
lovePercent = int(lovePercent)

if lovePercent < 10 or lovePercent > 90:
    print(f"Your score is {lovePercent}%, you go together like coke and mentos.")
elif lovePercent >= 40 and lovePercent <= 50:
    print(f"Your score is {lovePercent}%, you are alright together.")
else:
    print(f"Your score is {lovePercent}%.")