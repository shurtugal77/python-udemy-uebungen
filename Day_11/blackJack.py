############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playerCards = []
computerCards = []

def cardPicker():
    cardPicker = random.choice(cards)
    return cardPicker

def drawACard(playerCardArray):
    """Adds a card to the provided array. Calls the function 'cardpicker()' to get a random card."""
    playerCardArray.append(cardPicker())
    return playerCardArray


def sumOfCards(cardArray):
    return sum(cardArray)
    

def mustDrawAnotherCard(cardSum):
    if cardSum >= 17:
        return False
    return True

def makeAceToOne(cardArray):
    counter = 0
    # kann man auch mit .remove() machen
    for i in range(len(cardArray)):
        if cardArray[i] == 11 and counter < 1:
            cardArray[i] = 1
            counter += 1
    return cardArray


def playerChoiceEvaluation(choice):
    if choice == 'y':
            playerCards.append(cardPicker())
            print(f"You drew a {playerCards[-1]}")
            print(f"Your cards: {playerCards}")
            print(sumOfCards(playerCards))
    else:
        return False
    return True


# Initial Deal (2 Cards each)
for i in range(2):
    drawACard(playerCards)
    drawACard(computerCards)

print(f"Computers' first card: {computerCards[0]}")


autoRun = True
computerTurn = False
playerResult = ''

# Player chooses cards
while autoRun == True:
    playerSum = sumOfCards(playerCards)

    if playerSum > 21 and 11 in playerCards:
        input("You have an 11 in your deck - attempting to reduce card size - Continue with Enter")
        playerCards = makeAceToOne(playerCards)
        playerSum = sumOfCards(playerCards)
    elif playerSum > 21:
        playerResult = 'Lost'
        break

    if playerSum == 21:
        playerResult = 'Blackjack'
        break

    # See your cards
    print(f"Your cards: {playerCards}")
    print(f"Sum of your cards: {playerSum}\n")

    # if mustDrawAnotherCard(playerSum):
    #     input("You have to draw another card. Continue with 'Enter'. ")
    #     drawACard(playerCards)
    #     print(f"You drew a {playerCards[-1]}")
    # else:
    #     playerChoice = input("Do you want to draw another card? 'y' or 'n'? ").lower()
    #     autoRun = playerChoiceEvaluation(playerChoice)
    #     if autoRun == False: playerResult = 'computerTurn'
    
    playerChoice = input("Do you want to draw another card? 'y' or 'n'? ").lower()

    if playerChoice == 'y':
        drawACard(playerCards)
        print(f"You drew a {playerCards[-1]}")
    else:
        autoRun = playerChoiceEvaluation(playerChoice)
        if autoRun == False: playerResult = 'computerTurn'


if playerResult == 'Lost':
    print(f"AUTODEFEAT: You have lost. Your card sum is {playerSum} with your cards: {playerCards}")

elif playerResult == 'Blackjack':
    print(f"AUTOWIN: You won with a Blackjack! Your card sum is {playerSum} with your cards: {playerCards}")

elif playerResult == 'computerTurn':
    computerTurn = True
    print("Your turn is over: It's the computers turn now!\n")

# Computer chooses cards
computerResult = ''
while computerTurn:
    computerSum = sumOfCards(computerCards)

    if computerSum > 21 and 11 in computerCards:
        input("Computer has an 11 in your deck - attempting to reduce card size - Continue with Enter")
        computerCards = makeAceToOne(computerCards)
        computerSum = sumOfCards(computerCards)
    elif computerSum > 21:
        computerResult = 'Lost'
        break

    if computerSum == 21:
        computerResult = 'Blackjack'
        break
    
    # Wann entscheiden wir uns für ein draw?
    if computerSum == playerSum and playerSum == 20:
        computerResult = 'Draw'
        break

    # See computer
    print(f"Computer cards: {computerCards}")
    print(f"Sum of computers' cards: {computerSum}")

    if mustDrawAnotherCard(computerSum):
        input("Computer has to draw another card. Continue with 'Enter'. \n")
        drawACard(computerCards)
    elif computerSum < playerSum:
        drawACard(computerCards)
    elif computerSum > playerSum:
        computerTurn = False
        computerResult = 'Computer won over player'

if computerResult == 'Computer won over player':
    print(f"Computer had more eyes than you: {computerSum} | {computerCards} - YOU LOST! Player: {playerSum} | {playerCards}")

elif computerResult == 'Draw':
    print(f"It's a draw - WIP. Computer: {computerSum} | {computerCards}. Player: {playerSum} | {playerCards}")

elif computerResult == 'Lost':
    print(f"Computer had more than 21 and lost with {computerSum} | {computerCards} - YOU WON! Player: {playerSum} | {playerCards}")

elif computerResult == 'Blackjack':
    print(f"Wow the computer was lucky enough to get a Blackjack! {computerSum} | {computerCards} - YOU LOST!")






# exit while
    # Check ob player gegen computer verliert cards vs cards
    # spielneustart ermöglichen
































##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.