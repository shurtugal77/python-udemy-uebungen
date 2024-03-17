def primeCheck(number):
    if number <= 1:
        print("Not a PRIME NUMBER")
        return False

    for i in range(2, number//2+1):
        if number % i == 0:
            print("Not a PRIME NUMBER")
            return False
        
    print("It's a PRIME NUMBER")
    return True

numberToCheck = int(input('Enter a number: '))
primeCheck(numberToCheck)