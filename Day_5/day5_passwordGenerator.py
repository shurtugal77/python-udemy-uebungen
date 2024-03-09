#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easyPassword = ""
easyLetter = ""
easySymbol = ""
easyNumber = ""
randomPicker = 0

# Letters
for x in range(0, nr_letters):
    randomPicker = random.randint(0, len(letters))
    easyLetter += letters[randomPicker - 1]
# print(easyLetter)

# Symbols
for x in range(0, nr_symbols):
    randomPicker = random.randint(0, len(symbols))
    easySymbol += symbols[randomPicker - 1]
# print(easySymbol)

# Numbers
for x in range(0, nr_numbers):
    randomPicker = random.randint(0, len(numbers))
    easyNumber += numbers[randomPicker - 1]
# print(easyNumber)

easyPassword = easyLetter + easySymbol + easyNumber
print(easyPassword)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hardPassword = []
hardLetter = []
hardSymbol = []
hardNumber = []
randomPicker = 0

# Letters
for x in range(0, nr_letters):
    randomPicker = random.randint(0, len(letters))
    hardLetter.insert(x, letters[randomPicker - 1])   
# print(hardLetter)

# Symbols
for x in range(0, nr_symbols):
    randomPicker = random.randint(0, len(symbols))
    hardSymbol.insert(x, symbols[randomPicker - 1])
# print(hardSymbol)

# Numbers
for x in range(0, nr_numbers):
    randomPicker = random.randint(0, len(numbers))
    hardNumber.insert(x, numbers[randomPicker - 1])
# print(hardNumber)

# Shuffle the hard password
hardPassword = hardLetter + hardNumber + hardSymbol
random.shuffle(hardPassword)

# Convert to string
stringPassword = ""
for myChar in hardPassword:
    stringPassword += myChar

print(stringPassword)