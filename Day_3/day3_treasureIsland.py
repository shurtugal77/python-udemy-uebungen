print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

leftOrRight = input("Go left or right?\n").lower()

if leftOrRight == "right":
    print("Game Over")
elif leftOrRight == "left":
    swimOrWait = input("Do you want to swim or wait\n").lower()
    if swimOrWait == "swim":
        print("Game Over")
    elif swimOrWait == "wait":
        doorColour = input("Which door do you pick? Red, yellow or blue?\n").lower()
        if doorColour == "red" or doorColour == "blue":
            print("Game Over")
        elif doorColour == "yellow":
            print("You win lul!")




