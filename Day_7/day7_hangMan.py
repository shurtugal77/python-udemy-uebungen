from wonderwords import RandomWord

# Wir stellen jetzt den Spezialisten ein, der random Wörter generieren kann (Instanz)
wordGenerator = RandomWord()

# generate a random word
def getWord():
    return wordGenerator.word(word_min_length = 5, include_parts_of_speech=["nouns"])

# set lives
lives = 10

word = getWord().lower()


guessedLetters = []
def getLetterFromUser():
    letter = ""
    while len(letter) != 1 or letter in guessedLetters:
        letter = input("Give me a letter ").lower()
    guessedLetters.append(letter)
    return letter

def obscureWord(unobscuredWord, lettersToDisplay):
    obscuredWordList = []
    unobscuredLetterList = list(unobscuredWord.lower())
    for letter in unobscuredLetterList:
        if letter in lettersToDisplay:
            obscuredWordList.append(letter)
        else:
            obscuredWordList.append("_")
    return " ".join(obscuredWordList)


def printCurrentState():
    obscuredWord = obscureWord(word, guessedLetters)
    print(obscuredWord)
    print(f"\t\t\tGuessed already: {guessedLetters}")

print(word)

while lives > 0 and "_" in obscureWord(word, guessedLetters):
    printCurrentState()
    newLetter = getLetterFromUser()
    if newLetter in word:
        print(f"{newLetter} is in the word!")
    else:
        lives -= 1
        print(f"Lives remaining: {lives}")

if lives == 0:
    print(f"Get fucked, you lost. The word was {word}")
else:
    print(f"Congrats, the word was indeed {word}")

