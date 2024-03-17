import math

def paint_calc(height, width):
    result = (height * width) / coverage
    return math.ceil(result)

testHeight = int(input('Wallheight: '))
testWidth = int(input('Wallwidth: '))
coverage = 5

print(f'You need to buy {paint_calc(testHeight, testWidth)} cans')
