# Force definition of global variables in functions
def forceGlobal():
    global var
    var = "ick bin global"

forceGlobal()

print(var)


# Change (global) variables within functions
x = "super toller Wert"

def uiToll():
    global x
    x = "ein anderer Wert"

print(x)
uiToll()
print(x)


# Length of lists
itsMyList = ["deez", "nuts", 3, True]
print(len(itsMyList))


# Creating a list with the list constructor
thisList = list(("Apfel", "Banane", "Grapefruit"))
print(thisList)


# Accessing list items with range
rangeList = ["rot", "blau", "grün", "gelb", "orange", "lila", "schwarz"]
print(rangeList[1:5])
# 1 included : 5 excluded

# Check if item exists in list
checkList = ["apple", "banana", "cherry"]
if "apple" in checkList:
    print("Ja Junge, dat is dabei")

