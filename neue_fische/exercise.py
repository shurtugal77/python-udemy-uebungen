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

# copy lists
sourceList = ["apple", "banana", "cherry"]
copyList = sourceList.copy()
print(copyList)

# Alternate way with list()
sourceList = ["apple", "banana", "cherry"]
myList = list(sourceList)
print(myList)

# Alternate way with slice operator
myList = sourceList[:]
print(myList)

# Join lists easy
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Join with append()
for x in list2:
    list1.append(x)
print(list1)

# Join with extend()
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


# conditional statements
a = 33
b = 200
if b > a:
    print("b is greater than a")

# If with bool
isLoggedIn = True
if isLoggedIn:
    print("Was geht?")

# Elif
a = 33
b = 33
if b > a:
    print("B größer A")
elif a == b:
    print("beide gleich")

# Multi elif
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")


# Short if
a = 5
b = 2
if a > b: print("a ist größer")

# Short if with else
a = 2
b = 330
print("A") if a > b else print("B")

# if else variables
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# Multiconditions one line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Logical operators
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is true")

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")


# Combining logical operators
age = 25
isStudent = False
hasDiscountCode = True

if (age < 18 or age > 65) and not isStudent or hasDiscountCode:
    print("Discount applies!")

# Nested if statements
x = 41

if x > 10:
    print("Above ten")
    if x > 20:
        print("Above 20!")
    else:
        print("but not above 20!")

# Multiple levels if nesting
score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")

# Refactor multiple levels with logical operators
temperature = 25
isSunny = True

if temperature > 20:
    if isSunny:
        print("Nice day for fishing ain't it")

# Same example with and
if temperature > 20 and isSunny:
    print("Nice day for fishing ain't it")


# Pass statement
a = 33
b = 200

if b > a:
    pass

# While loop with break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# While with continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# While with else
anzahlPfannkuchen = 0
while anzahlPfannkuchen < 10:
    print("Pfannkuchen:" + str(anzahlPfannkuchen))
    anzahlPfannkuchen += 1
else:
    print("Wir haben mindestens 10 Pfannkuchen")

# For loop with string
for x in "banana":
    print(x)

# For loop with break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# For with continue
for x in fruits:
    if x == "banana":
        continue
    print(x)

# For and range(custom start, end, step)
for x in range(2, 30, 2):
    print(x)

# For with else:
for x in range(6):
    print(x)
else:
    print("Finally done!")

# Nested for
adjectives = ["red", "big", "nice"]
fruits = ["apple", "banana", "cherry"]

for x in adjectives:
    for y in fruits:
        print(x, y)


# Function example
def fahrenheitToCelsius(fahrenheit):
    return ((fahrenheit - 32) * 5) / 9

print(fahrenheitToCelsius(77))

# Argument vs parameter
def kaffeeKochen(bohnen): #bohnen ist ein Parameter
    return print(str(bohnen) + "x Heißer Kaffee")

kaffeeKochen(200) #200 ist ein Argument


# Standard parameter example
def fragPicard(antwort = "fiese Fresse"):
    print("Ey - ", antwort)

fragPicard("Wie spät ist es?")
fragPicard()

# Key value arguments
def tierNamen(animal, name):
    print("Ich bin ein/e", animal)
    print("Der name meines/r", animal + " ist:", name)

tierNamen(animal="Giraffe", name="Superidiot")

# Positional arguments - absichtlich vertauscht
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("Buddy", "dog")  

# Mixed arguments
def exmapleFunc(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

exmapleFunc("dog", name="DeezNuts", age=69)


# Datatypes in functions:
def myFunction(fruits):
    for fruit in fruits:
        print(fruit)

myFruits = ["cherry", "apple", "banana"]
myFunction(myFruits)

# Example - dictionary to a function
def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person) 


# Forcing positional arguments
def forcedPositionalArguments(name, /):
    print("Hi, mein Name ist", name)

forcedPositionalArguments("Robert")


# Forcing keyword arguments
def forcedPositionalArguments(*, name):
    print("Hi, mein Name ist", name)

forcedPositionalArguments(name="Robert")


# Mixed forced arguments
def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result) 


# *args
def ichWeißNochNicht(*items):
    print("Ich habe 10", items[1])
    print("Und auch 20", items[0]) #zweiter tuple Wert

ichWeißNochNicht("Bananen", "Nüsse", "Himbeeren")

# args example with sum function
def calculateMax(*numbers):
    result = 0
    for value in numbers:
        result += value
    return result

print(calculateMax(1,2,3))
print(calculateMax(10,5))
print(calculateMax(10,205,30,4))

# **Keywordarguments
def sayName(**names):
    print("Hello my name is " + names["fname"])

sayName(fname = "Robert", lname = "Nuts")

# Accessing keyword arguments (dictionary)
def myFunction(**myvar):
    print("Type", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

myFunction(name = "Robert", age = 36, city = "Regensburg")

# Combining regular arguments with **kwargs
def printUserData(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

printUserData("robert420", age = 25, city = "Oslo", hobby = "coding")

# Combining everything lol
def getUserInfo(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

getUserInfo("Dr. Goaßmaß", "Robert", "Rebecca", age = 69, city = "Oslo")

# Unpacking list arguments
def summarize(a, b, c):
    return a + b + c 

numbers = [1, 2, 3]
result = summarize(*numbers) # === summarize(1, 2, 3)
print(result)

# Unpacking dictionary arguments
def getName(fname, lname):
    print("Hello", fname, lname)

personData = {"fname": "Robert", "lname": "Geißmeiß"}
getName(**personData) # === getName(fname="Robert", lname="Geißmeiß")

# Create global variable in function
def localFunction():
    global wowGlobal
    wowGlobal = 300

localFunction()
print(wowGlobal)

# Nonlocal variable in nested functions
def function1():
    x = 5
    def function2():
        nonlocal x
        x = "deez"
    function2()
    return x

print(function1())

# Basic Decorator
def changeCase(inputFunction):
    def inner():
        return inputFunction().upper()
    return inner

@changeCase
def normalFunction():
    return "Hallo - das ist klein aber wird groß"

@changeCase
def otherFunction():
    return "Schreib das mal groß Junge!"

print(normalFunction())
print(otherFunction())


# Decorators with arguments
def changeCase(inputFunction):
    def inner(x):                       # x = passed argument (name) to wrapper
        return inputFunction(x).upper()
    return inner

@changeCase
def sayHello(name):
    return ("Hello " + name)

print(sayHello("Robert"))

# Secured Decorator
def changeCase(inputFunction):
    def inner(*args, **kwargs):
        return inputFunction(*args, **kwargs).upper()
    return inner

@changeCase
def sayHello(name):
    return ("Hello " + name)

print(sayHello("Secured Robert"))


# Decorator with it's own arguments
def changeCase(decoratorArgument):
    def changeCase(inputFunction):
        def inner():
            if decoratorArgument == 1:
                a = inputFunction().lower()
            else:
                a = inputFunction().upper()
            return a
        return inner
    return changeCase

@changeCase(1)
def sayMyName():
    return "HELLO LOWERCASE ROBERT"

print(sayMyName())


# Multiple decorators
def changeCase(inputFunction):
    def inner():
        return inputFunction().upper()
    return inner

def addGreeting(inputFunction):
    def inner():
        return "Hello there " + inputFunction() + " Nice day for fishing, ain't it?!"
    return inner
    
@changeCase
@addGreeting
def getName():
    return "Robert"

print(getName())

# Accessing metadata of functions
def metaDataTest():
    return "Wow dis is cool"

print(metaDataTest.__name__)


# Preserving metadata
import functools

def changeCase(inputFunction):
    @functools.wraps(inputFunction)
    def inner():
        return inputFunction().upper()
    return inner

@changeCase
def greetMe():
    return "Hello, have a nice day!"

print (greetMe.__name__)


# Lambda functions
x = lambda a : a + 10
print(x(5))

x = lambda a,b : (a * b)+2
print(x(5,10))

# Lambda function use case as anonymous function within a function
def regularFunction(n):
    return lambda a : a * n

doubleMyInput = regularFunction(2)
trippleMyInPut = regularFunction(3)

print(doubleMyInput(11))
print(trippleMyInPut(11))

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x : x * 2, numbers))
print(doubled)

# Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Lambda with sorted()
students = [
    ("Emil", 25),
    ("Tobias", 22),
    ("Linus", 28)
]

sorted_students = sorted(students, key=lambda x : x[1])
# sorts the list of tuples by the second element
print(sorted_students)

# Another sorted() examples
words = [
    "apple",
    "pie",
    "banana",
    "cherry"
]

sorted_words = sorted(words, key=lambda x : len(x))
# sorts the list based on its strings length
print(sorted_words)


# Recursion example counting down from 5
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)

# Recursion with base and recursive case commented
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

# Fibonacci Sequence
# Eine Zahl ist die Summe der zwei vorhergehenden, Start mit 0 und 1
def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

# Recursion with lists
# Calculate the sum of all elements in a listy
def sumList(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sumList(numbers[1:])

myList = [1, 2, 3, 4, 5]
print(sumList(myList))

# Recursion with lists - find maximum value
def findMax(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        maxOfRest = findMax(numbers[1:])
        return numbers[0] if numbers[0] > maxOfRest else maxOfRest

myList = [3, 7, 2, 9, 1]
print(findMax(myList))

import sys
print(sys.getrecursionlimit())

# Generator basic example
def myGenerator():
    yield 1
    yield 2
    yield 3

for value in myGenerator():
    print(value)

print("")

# Another generator example
def countUpTo(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in countUpTo(5):
    print(num)

# Memory efficient generator
def largeSequence(n):
    for i in range(n):
        yield i

# This doesn't create a million numbers in memory
gen = largeSequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

# Generators with next
def simpleGenerator():
    yield "Robert"
    yield "Rebecca"
    yield "Samuel"

gen = simpleGenerator()
print(next(gen))
print(next(gen))
print(next(gen))

# Generators exception testing
def simple_gen():
    yield 1
    yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
#print(next(gen)) # This will raise StopIteration 


# Generator Expressions
# List comprehension for comparison
listComp = [x * x for x in range(5)]
print(listComp)

# Generator expression - creates a generator
genExp = (x * x for x in range(5))
print(genExp)
print(list(genExp))

# Generator expression with "sum"
# Calculate the sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)

print("")

# Fibonacci sequence generator - memory efficient
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b =  b, a + b
#Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(10):
    print(next(gen))

# Generator send()
def echoGenerator():
    while True:
        received = yield
        print("Received:", received)

gen = echoGenerator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")


# Generator close()
def myGen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")

gen = myGen()
print(next(gen))
gen.close()