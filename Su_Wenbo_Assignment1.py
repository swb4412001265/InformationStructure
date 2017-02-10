# Su_Wenbo_Assignment1
# Initilize list
NOUNS = ["time", "year", "people", "way", "day", "man", "thing", "woman"]
VERBS = ["pay", "put", "read", "run", "say", "see"]
ADJECTIVES = ["other", "new", "good", "high", "old"]
SENTENCES = ["Man verb on a adjective noun.", "Noun verb to the adjective ground.",
             "All the king’s adjective horses and all the king’s dainty noun could not verb scrambled egg man back together again."]
completedSentences = []     # Create a list for storing picked sentences
# Validate user input
validInputFlag = True
while validInputFlag:
    # Prompt user for a number.
    userInput = input("Please input a positive integer:\n")
    try:
        inputInteger = int(userInput)  # Store user's input
    except ValueError:  # Check if input is not number
        continue
    else:
        if inputInteger < 0:    # input must be greater than 0
            continue
        else:
            indexNOUNS = inputInteger % len(NOUNS)  # Calculate and assign index of list
            indexVERBS = inputInteger % len(VERBS)
            indexADJECTIVES = inputInteger % len(ADJECTIVES)
            indexSENTENCES = inputInteger % len(SENTENCES)
            pickedSentence = SENTENCES[indexSENTENCES]
            pickedSentence = pickedSentence.lower()    # In case the first letter is the key word(NOUNS, ADJECTIVE or VERB)
            pickedSentence = pickedSentence.replace("noun", NOUNS[indexNOUNS])     # replace noun in the sentence with picked noun
            pickedSentence = pickedSentence.replace("verb", VERBS[indexVERBS])
            pickedSentence = pickedSentence.replace("adjective", ADJECTIVES[indexADJECTIVES])
            pickedSentence = pickedSentence.capitalize()   # Put the first letter back to capital
            if pickedSentence in completedSentences:    # Check if sentence has been picked before
                print("This sentence has been picked.\n")
            else:
                completedSentences.append(pickedSentence)
            for indexSENTENCES in range(len(completedSentences)):    # print all the sentences in the compleated list
                print(completedSentences[indexSENTENCES])
            validInputFlagAgain = True
            while validInputFlagAgain:
                userInputPlayAgain = input("Do you want to keep playing? (y or n)\n")   # Ask user if want to play again
                if userInputPlayAgain == 'y':
                    break
                elif userInputPlayAgain == 'n':     # if no then set flag to false and end the program
                    validInputFlag = False
                    break
                else:       # For the other situations, keep entering option
                    continue




