# Calculator
import os

# Add
def calcAdd(number1, number2):
    result = number1 + number2
    return result

# Subtract
def calcSubstract(number1, number2):
    result = number1 - number2
    return result

# Multiply
def calcMultiply(number1, number2):
    result = number1 * number2
    return result

# Divide
def calcDivide(number1, number2):
    result = number1 / number2
    return result

operations = {
    '+': calcAdd,
    '-': calcSubstract,
    '*': calcMultiply,
    '/': calcDivide
}

def calculator():
    autoRun = True
    number1 = None

    while autoRun:
        
        if number1 is None:
            number1= float(input("What's your first number?: "))
        else:
            number1 = answer
            print(f"First number is {number1}.")

        for keys in operations:
            print(keys)

        operationSymbol = input("Pick an operation from the line above: ")
        number2= float(input("What's your second number?: "))

        calcFunction = operations[operationSymbol]
        answer = calcFunction(number1, number2)

        print(f"{number1} {operationSymbol} {number2} = {answer}") 

        continueCalculation = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation.: ")
        if continueCalculation == 'n':
            autoRun = False
            os.system('cls')
            calculator()

        os.system('cls')

calculator()
