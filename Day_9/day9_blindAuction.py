import os

os.system('cls')

allBids = {}
autoRun = True
highestBid = 0
highestBidder = ''

while autoRun == True:
    myName = str(input("Please enter your name: "))

    myBid = int(input("Please enter your bid price: "))
    myBidEuro = str(myBid) + '€'
    print(f"Your bid is {myBidEuro}")

    allBids[myName] = myBid

    userChoice = str(input("Are there other users, who want to bid? [yes/no] "))
    if userChoice == "no":
        autoRun = False
    os.system('cls')

for names in allBids:
    
    if highestBid < allBids[names]:
        
        highestBid = allBids[names]
        highestBidder = names

print(f"Congratiolations {highestBidder}, you won the opportunity to pay the highest bid of {highestBid}.")

print(f"All bids are: {allBids}")