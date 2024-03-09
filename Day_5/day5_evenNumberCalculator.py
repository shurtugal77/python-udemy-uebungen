target = int(input())

# Only sum up even numbers to target. 0 + 2 + 4 ... +
mySum = 0
for currentNumber in range(0, target + 1, 2):
    mySum += currentNumber

print(mySum)