def greet():
    print("Hello - how are your ballz?")
    print('Deez nuts seem nice on your chin.')
    print('How about some nuts on your face?')

greet()

def greetWithName(name):
    print(f'Hello {name}, how are your ballz?')
greetWithName('Robert')


# def myFunction(PARAMTER):
#    ...
# myFunction(ARGUMENT)

# def myFunction(PARAMTER = ...) --> Standardwert zuweisen


def greetWithNameLocation(name, location):
    print(f'Hello {name}, your ballz are living in {location} - but not on my chin.')

greetWithNameLocation('Robert', 'Regensburg') # Positional argument


# Keyword arguments

def greetWithArguments(name, location):
    print(f'Hello {name} - deez nuts are in {location}')

greetWithArguments(location='Regensburg', name='Robert')

