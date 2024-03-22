import os

os.system('cls')


auctionIsOpen = True
collectedBids = {}

while auctionIsOpen == True:
    name = ''
    while len(name) <= 0:
        name = input("Please enter your name.\n")
    bid = 0
    while bid == 0:
        bid = input("Please enter your bid.\n")
        try:
            bid = int(bid)
        except ValueError:
            bid = 0
    
    collectedBids[name] = bid
    os.system('cls')

    if input("Do you want to continue? Type \"no\" to exit.\n").lower() == "no":
        auctionIsOpen = False
    os.system('cls')

maxBid = 0
maxBidder = []
for bidderName in collectedBids:
    bid = collectedBids[bidderName]
    if bid > maxBid:
        maxBid = bid
        maxBidder = [bidderName]
    elif bid == maxBid:
        maxBidder.append(bidderName)

if len(maxBidder) == 1:
    print(f"The winner is {maxBidder[0]} with their bid of {maxBid}.")
else:
    print(f"There was a tie between {" and ".join(maxBidder)} who all bid {maxBid}. You guys are lame.")

print(collectedBids)
print(maxBid)
print(maxBidder)