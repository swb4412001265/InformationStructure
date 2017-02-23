'''
This file is a template that may be used for Assignment 2.  The intent is to supply
you with some code so you can focus on the new items in the program
'''
import operator
import os
import random
import csv

currDir = os.getcwd()
fileFolder = os.path.join(currDir,"resources")
if os.path.exists(fileFolder) == False:
    os.makedirs(fileFolder)

def load_csv_to_list(path_to_file):
    filePath = os.path.join(fileFolder, path_to_file)
    #Validate Path to file exists
    if os.path.exists(filePath) == False:
        print("Path to file does not exist!\n")
        quit()
    #Validate file exists
    elif os.path.isfile(filePath) == False:
        print("File does not exist!\n")
        quit()
    #Return a list of items from file
    else:
        readList = []
        with open(filePath, 'r') as readFile:
            readLine = csv.reader(readFile)
            readLine = list(filter(None, list(readLine)))
            readFile.close()
            for Line in readLine:
                Line = ''.join(Line)
                readList.append(Line)
        return readList



def shuffle(sequence):
    """Returns a shuffled list"""
    length = len(sequence)
    #Write the code that will take a list and shuffle it randomly
    randomNumList = []
    newSequence = []
    while len(randomNumList) != length:
        randomNum = random.randint(0, length - 1)
        if randomNum not in randomNumList:
            randomNumList.append(randomNum)
    for randomIndex in randomNumList:
        newSequence.append(sequence[randomIndex])
    return newSequence



def load_mad_lib_resource(path_to_resource):
    #Call load_csv_to_list
    #Verify the file exists
    filePath = os.path.join(fileFolder, path_to_resource)
    if os.path.exists(filePath) == False:
        print("Path to file does not exist!\n")
        quit()
    #Return a tuple of the shuffled list
    return tuple(shuffle(load_csv_to_list(path_to_resource)))

def play_game(user_sentences,lower_bound, upper_bound):
    is_keep_playing = None

    while is_keep_playing != 'n':
        user_str_number = input(
            "Please provide a number between {} and {}".format(lower_bound, upper_bound)
    )

        try:
            user_number = int(user_str_number.strip().lower())
        except:
            print("Sorry the value provided is not an integer.")
            user_number = None
            continue

        if user_number is not None:
            if user_number < MIN_VALUE:
                print("Sorry the number provided is too small (lower than {})".format(MIN_VALUE))
                continue
            elif user_number > MAX_VALUE:
                print("Sorry the number provided is too big (greater than {})".format(MAX_VALUE))
                continue
            else:
                sentence_idx = random.randint(user_number, MAX_VALUE) % len(SENTENCES)
                noun_idx = random.randint(user_number, MAX_VALUE) % len(NOUNS)
                verb_idx = random.randint(user_number, MAX_VALUE) % len(VERBS)
                adjective_idx = random.randint(user_number, MAX_VALUE) % len(ADJECTIVES)

        # generate the mad lib sentence
                sentence = SENTENCES[sentence_idx].format(
                noun=NOUNS[noun_idx],
                verb=VERBS[verb_idx],
                adjective=ADJECTIVES[adjective_idx],
        )

        #GENERATE THE SENTENCES AND WRITE TO THE FILE IF NOT ALREADY SAVED
        if sentence not in user_sentences:
            user_sentences.append(sentence)
            user_sentences.sort()
            fileSentence = os.path.join(currDir, "SENTENCE" + userName + ".csv")
            with open(fileSentence, 'w') as writeFile:
                for index in range(len(user_sentences)):
                    writeFile.write("{},{} \n".format(user_sentences[index], index + 1))
                writeFile.close()
        else:
            print("This sentence has been picked.\n")
        #PRINT ALL OF THE SENTENCES FOR THE USER THUS FAR
        for sentence in user_sentences:
            print(sentence + '\n')
        is_keep_playing = None  # reset

        while 'y' != is_keep_playing and 'n' != is_keep_playing:
            is_keep_playing = input("Do you want to keep playing? y / n")
            try:
                is_keep_playing = is_keep_playing.strip().lower()
            except:
                is_keep_playing = None

            if 'y' != is_keep_playing and 'n' != is_keep_playing:
                print("Sorry, I did not get that.")


# GET THE LISTS FROM THE FILES
ADJECTIVES = load_mad_lib_resource("CS521_assignment2_adjectives.csv")
NOUNS = load_mad_lib_resource("CS521_assignment2_nouns.csv")
SENTENCES = load_mad_lib_resource("CS521_assignment2_sentences.csv")
VERBS = load_mad_lib_resource("CS521_assignment2_verbs.csv")
#VERIFY THE LISTS EXIST

# boundaries
MIN_VALUE = 0
MAX_VALUE = max(
        len(SENTENCES),
        len(NOUNS),
        len(VERBS),
        len(ADJECTIVES),
)

# user's mad lib
user_sentences = []

#PROMPT FOR USERNAME

userName = input("Please input your username:\n")
#VERIFY THE A USER NAME WAS ENTERED ELSE EXIT THE PROGRAM
if not userName:
    print("There is no username!")
    quit()
#FIND OUT IF THERE IS AN EXISTING USER SAVED GAMES
fileSentence = os.path.join(currDir, "SENTENCE" + userName + ".csv")
if os.path.isfile(fileSentence) == True:
    with open(fileSentence, 'r') as readFile:
        for line in readFile:
            line = line.split(",")
            user_sentences.append(line[0])
        readFile.close()
    print(user_sentences)

#GET THE USER'S SAVED GAMES IF IT EXISTS

#SORT THE USER SENTENCES
user_sentences.sort()
#CALL PLAY GAME FUNCTION
play_game(user_sentences, MIN_VALUE, MAX_VALUE)
print("Bye!")
