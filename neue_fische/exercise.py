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


# Change items in lists
thisList = ["rot", "blau", "grün", "gelb", "orange", "lila", "schwarz"]
thisList[1:4] = ["lila", "buchweizen", "samuel"]
print(thisList)


# Append list elements
thisList.append("UwU")
print(thisList)


# Extend a list with another list
numberList = ["1", "2", "3", "4", "5"]
thisList.extend(numberList)
print(thisList)


# Remove elements of a list
thisList.remove("UwU")
print(thisList)


# Remove elements with pop
tolleListe = ["nudeln", "eier", "gurken", "erbsen"]
tolleListe.pop()
print(tolleListe)

# Remove items with del
del tolleListe[0]
print(tolleListe)

# Delete entire list
del  tolleListe

# Clear a list
einkaufsListe = ["eier", "mehl", "zucker", "salami"]
einkaufsListe.clear()
print(einkaufsListe)