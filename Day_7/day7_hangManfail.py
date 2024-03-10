from wonderwords import RandomWord

# Wir stellen jetzt den Spezialisten ein, der random Wörter generieren kann (Instanz)
wordGenerator = RandomWord()

# generate a random word
def getWord():
    return wordGenerator.word(word_min_length = 5, include_parts_of_speech=["nouns"])

print(getWord())



# # Is letter in word (Letter and Position)?
# def whereIsLetterInWord(wordToCheck, Letter):
#     lowerCaseWord = wordToCheck.lower()
#     foundPosition = []

#     for x in range(0, len(lowerCaseWord)):

#         if lowerCaseWord[x] == Letter:
#             foundPosition.append(lowerCaseWord[x])
#             foundPosition.append(x)
# # Gibt den Buchstaben gefolgt von der Positon an denen einen Buchstabe gefunden wurde nullindexbereinigt zurück
#     return foundPosition


# # obscure a word.gibt das Wort mit versteckten Buchstaben zurück. Aus "Esel" wird mit geratenem "s": "_ s _ _"

# def obscureWord(word, guessedLetters):
    
#     # Word in Liste umwandeln damit einzelne Buchstaben replaced werden können - oder vorher googlen und "replace" nutzen ... :(
#     wordList = list(word)

#     for x in range(0, len(guessedLetters)):
        
#         result = whereIsLetterInWord(word,guessedLetters[x])
        
#         # Integer von "result" abfragen um die Stellen zu wissen, an denen "_" gesetzt werden soll.
#         for y in range(1, len(result), 2):
            
#             if isinstance(result[y], int):
                
#                 # Direkt auf den Index von Result zugreifen, weil wir wissen ja wo ein Buchstabe geflippt werden soll
#                 wordList[result[y]] = "_"
        
#         word = "".join(wordList)
        
#         # Anschalten um zu sehen wo der Buchstabe gefunden wurde. Beispiel: "Mahballz" "l, a" => ["l", 5, "l", 6] ["a", 1, "a", 4]
#         # print(result) 
        
#         # Anschalten um das Zwischenergebnis von "Mah__alz" zu sehen
#         # print(word)
#     return word


print(obscureWord("Mahballz",["l", "a"]))