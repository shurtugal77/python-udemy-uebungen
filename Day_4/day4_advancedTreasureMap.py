
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Wo soll der Schatz versteckt werden Captain?\n") # Where do you want to put the treasure

#Check row number
tresNumber = int()
if position[1] == "1":
    tresNumber = 1
elif position[1] == "2":
    tresNumber = 2
elif position[1] == "3":
    tresNumber = 3

#Check column character
tresChar = int()
if position[0] == "A":
    tresChar = 1 
elif position[0] == "B":
    tresChar = 2
elif position[0] == "C":
    tresChar = 3

#Set "X" on map
map[tresNumber-1][tresChar-1] = "X"

# Check map
print(f"{line1}\n{line2}\n{line3}")