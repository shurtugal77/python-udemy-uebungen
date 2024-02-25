import random

print("Rock Paper Scissors! What do you choose?\n")
choiceNames = ["Rock", "Paper", "Scissors"]

# User choice
userChoice = int(input("Type 0 for 'Rock', 1 for 'Paper' and 2 for 'Scissors'\n"))
print(f"You chose {choiceNames[userChoice]}")

# Computer choice
computerChoice = random.randint(0, 2)
print(f"Computer chose {choiceNames[computerChoice]}")

# Spielausgang berechnen
combinedChoices = str(userChoice) + str(computerChoice)

userWinCondition = ["02", "10", "21"]
userLoseCondition = ["01", "12", "20"]
drawCondition = ["00", "11", "22"]

if combinedChoices in userLoseCondition:
    print("You loose")
elif combinedChoices in userWinCondition:
    print("You win")
elif combinedChoices in drawCondition:
    print("Draw - Play again.")

# Draw vorher prüfen, dann nur auf loose oder win prüfen sonst Gegenteil ausgeben.