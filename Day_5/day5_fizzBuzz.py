# # Fizz Buzz - Robert Lösung
# currentNumber = 0
# for currentNumber in range(1, 100 + 1):

#     # Divideable by 3 = "Fizz"
#     if currentNumber % 3 == 0:
#         print("Fizz")

#         # Divideable by 3 and 5 = "FizzBuzz"
#         if currentNumber % 5 == 0:
#             print("FizzBuzz")

#     # Divideable only by 5
#     elif currentNumber % 5 == 0:
#         print("Buzz")

#     # Divideable by neither
#     else:
#         print(currentNumber)


# Bessere Lösung

currentNumber = 0
for currentNumber in range(1, 100 + 1):
    text = ""
    # Divideable by 3 add "Fizz"
    if currentNumber % 3 == 0:
        text += "Fizz"

    # Divideable by 5 add "Buzz"
    if currentNumber % 5 == 0:
        text += "Buzz"
    
    # Not divideable, therefore -> print number
    if text == "":
        print(currentNumber)    
    # Was dividable, therefore -> print text
    else:
        print(text)   
