# Total bill
tableBill = float(input("Für wie viel Geld habt ihr denn schon wieder Sushi gegessen?\n"))
#tableBill = 124.56

# Percentage tip
tipPercentage = int(input("Wie viel Trinkggeld darf es sein? 10, 12 oder 15%\n"))
tipFloat = 1 + tipPercentage / 100

# How many people to split the bill with
peopleAmount = int(input("Wie viele Leute haben sich den Ranzen vollgehauen?\n"))

# Each person should pay
totalBill = tableBill * tipFloat
billPerPerson = round(totalBill / peopleAmount, 2)

# Nachkommazahlen beim Runden
formatedBillPerPerson = "{:.2f}".format(billPerPerson)

print(f"Jeder von euch Nassbirnen zahlt jetzt bitte mal ${formatedBillPerPerson}")