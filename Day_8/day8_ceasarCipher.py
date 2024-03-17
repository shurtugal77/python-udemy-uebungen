alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = ''
while direction != 'encode' and direction != 'decode':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def shiftOverflow(shift):
    moduloIndex = shift % 26

    return moduloIndex

def shiftLetter(letter, shift):
    letterIndex = alphabet.index(letter)
    shiftIndex = letterIndex + shift

    shiftIndex = shiftOverflow(shiftIndex)
    
    return alphabet[shiftIndex]


def encrypt(text, shift):
    encryptedText = []

    for i in range (0, len(text)):
        if text[i] in alphabet:
            encryptedText.append(shiftLetter((text[i]), shift))
        else:
            encryptedText.append(text[i])

    encryptedString = ''.join(encryptedText)
    return encryptedString


if direction == 'encode':
    print(encrypt(text=text, shift=shift))
elif direction == 'decode':
    print(encrypt(text=text, shift= -1 * shift))




    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.