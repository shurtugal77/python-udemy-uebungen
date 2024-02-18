# Even / Odd check

yourNumber = int(input("Tell me your number as integer.\n"))

divisonModulo = yourNumber % 2

if divisonModulo != 0:
    print("Your number is odd")
else:
    print("Your number is even")