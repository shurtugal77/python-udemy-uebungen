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


# Loop throug a list
einkaufsListe = ["eier", "mehl", "zucker", "salami"]
for x in einkaufsListe:
    print(x)

print(" ")
# Loop with len/range
for i in range(len(einkaufsListe)):
    print(einkaufsListe[i])

print(" ")
# Loop with while
einkaufsListe = ["eier", "mehl", "zucker", "salami"]
i = 0
while i < len(einkaufsListe):
    print(einkaufsListe[i])
    i += 1


# List comprehension
einkaufsListe = ["eier", "mehl", "zucker", "salami"]
[print(x) for x in einkaufsListe]


# List comprehension example
# Traditional
fruits = fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# 1 Liner
fruits = fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


# List comprehension with iterable examples
newlist = [x for x in range(10)]
print(newlist)

# With condition - only numbers smaller than 5
newlist = [x for x in range(10) if x < 5]
print(newlist)


# Manipulate expression
newlist = [x.upper() for x in fruits]
print(newlist)


#Condition in expression
# Only output fruits other than "banana" - replace "banana" with "orange"
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


# Sort list
sortlist = ["orange", "mango", "kiwi", "pineapple", "banana"]
sortlist.sort()
print(sortlist)
#Reverse sort
sortlist.sort(reverse=True)
print(sortlist)


# Create custom sorting function
# Returns absolute number, sorting with lowest number first
def mySortingFunction(n):
    return abs(n - 50)

soManyNumbers = [100, 50, 65, 82, 23]
soManyNumbers.sort(key = mySortingFunction)
print(soManyNumbers)


# Case insensitive sorting
insensList = ["banana", "Orange", "Kiwi", "cherry"]
insensList.sort(key = str.lower)
print(insensList)


# Reverse Sorting
sortlist = ["orange", "mango", "kiwi", "pineapple", "banana"]
sortlist.reverse()
print(sortlist)

