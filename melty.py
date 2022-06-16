"""
This program is analogous to Hangman. User keeps guessing the word
with every wrong attempt a snowman melts till user runs out of attempts
or till they guess the word.
Name: Andrew Henin
Date: April 2022
"""

from random import *

def main():

    answerList = wordGen()
    # answerList is a list with the characters of the to-be-guessed word.
    correctList = ["-"]*len(answerList)
    # this is a list with the correct guessed characters.
    guessList = []
    # an accumulator list with all the guessed characters: the correct and incorrect ones.
    guessLeft = 8
    # this is a variable holding the total number of guesses
    melty = createMelty()
    # this function creates Melty
    welcome()

    for i in range(13):
        print(melty[i])

    while not gameOver(guessLeft, correctList):
        printGame(guessLeft, correctList)
        #It includes the incomplete/complete word and how many attempts remaining
        guess = input("Enter a letter: ")
        guess = isValid(guess, guessList)
        #It gets an input and checks for it if it’s valid
        if checkGuess(guess, correctList, answerList) == False:
                guessLeft = guessLeft - 1
        printMelty(melty, guessLeft)

    printOutMsg(correctList, answerList, guessLeft)
    # it calls check if won or loss which prints th()e final msg either loss or win


def welcome():
    """
    This function prints the welcome message.
    """
    print()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("This program plays a game of Melty.\n")
    print("Guess letters in the mystery word.")
    print("You can only make 8 incorrect guesses before")
    print("Melty melts.  See if you can save Melty and")
    print("guess the word before you run out of guesses.\n")
    print("              Good Luck!              ")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print()


def wordGen():
    """
    This function reads the words file
    It generates a random word from it
    returns: a list of characters answerList = [ch’s in word]
    """

    infile = open("/usr/local/doc/wordfile.txt")
    lines = infile.readlines()
    answer = choice(lines)
    answer = answer.rstrip()
    answerList = []

    for i in range(len(answer)):
        answerList.append(answer[i])

    # print(answerList)

    return answerList


def printGame(guessLeft, correctList):
    """
    It prints the updated guess.
    It also includes how many attempts remaining
    guessLeft is the number of remaining guesses
    correctList is a list of the correct guessed characters of the word
    """

    word = ""
    for i in range(len(correctList)):
        word = " ".join(correctList)
    print()
    print()
    print("word: %s" % (word))
    print()
    print("Incorrect guesses left: %d" % (guessLeft))
    print()



def isValid(guess, guessList):
    """"
    It gets an input and checks if it’s valid
    correctList is a list of the correct guessed characters of the word
    guessList is the list of all guess characters whether right or wrong
    return: guess
    """

    while (guess.isalpha() == False) or (len(guess) != 1) or (guess in guessList):

        if guess.isalpha() == False or len(guess) != 1:
            print("  hey, '%s' isn't an alphabetic character, try again..." % (guess))
            guess = input("Enter a letter: ")

        if guess in guessList:
            print("  you already guessed '%s', try again..." % (guess))
            print()
            guess = input("Enter a letter: ")


    guess = guess.lower()
    guessList.append(guess)

    return guess



def checkGuess(guess, correctList, answerList):
    """"
    It contains a for loop to check for the letter in the word
    and prints if the charachter is in word or not
    guess is the guessed character
    correctList is a list of the correct guessed characters of the word
    answerList is the list of the characters of the answer word
    returns a boolean value True or False depending on whether the guessis correct
    """

    index = []
    # this is an accumulator list

    if guess in answerList:
        print("  good guess, '%s' is in the word." % (guess))
        print()
        print()
        for i in range(len(answerList)):
            if guess == answerList[i]:
                index.append(i)
                for j in index:
                    correctList[j] = answerList[j]

        return True

    else:
        print("  sorry there is no '%s' in the word." % (guess))
        print()
        print()
        return False


def gameOver(guessLeft, correctList):
    """
    This function checks if game is over.
    guessLeft is the number of remaining guesses
    correctList is a list of the correct guessed characters of the word
    returns boolean value True or False
    """

    if guessLeft == 0:
        return True

    if "-" not in correctList:
        return True

    return False


def printOutMsg(correctList, answerList, guessLeft):
    """
    This function calls winOrLoss
    and prints the final msg
    correctList is a list of the correct guessed characters of the word
    """
    word = "".join(answerList)
    if winOrLoss(guessLeft) == True:
        print()
        print()
        print("You won!!! The word was %s. You saved Melty!" % (word))
    else:
        print()
        print()
        print("Sorry, Melty melted.  The word was: %s. \
 Better luck next time!" % (word))


def winOrLoss(guessLeft):
    """
    guessLeft is the number of guesses left
    """

    if guessLeft == 0:
        return False
    else:
        return True


def createMelty():
    """
    This function has all the possible components of Melty
    It draws Melty as a list and returns it to main()
    returns: melty
    """

    part1 = "          -----          "
    part2 = "          |   |          "
    part3 = "       -----------       "
    part4 = "         | * * |         "
    part5 = "         |  o  |         "
    part6 = "         -------         "
    part7 = " \      |   x   |     /  "
    part8 = " -------|   x   |------- "
    part9 = " /      |   x   |     \  "
    par10 = "       ------------      "
    par11 = "       |          |      "
    par12 = "       |          |      "
    par13 = "       ------------      "

    par14 = " \      |       |     /  "
    par15 = " -------|       |------- "
    par16 = " /      |       |     \  "

    par17 = "         -------         "
    par18 = " \      |       |        "
    par19 = " -------|       |        "
    par20 = " /      |       |        "
    par21 = "         -------         "

    par22 = "         -------         "
    par23 = "        |       |        "
    par24 = "        |       |        "
    par25 = "        |       |        "
    par26 = "         -------         "

    par27 = "         | * * |         "
    par28 = "         |  o  |         "

    par29 = "         |     |         "
    par30 = "         |     |         "


    melty = [part1, part2, part3, part4, part5, part6, part7, part8, part9,
    par10, par11, par12, par13, par14, par15, par16, par17, par18, par19, par20,
    par21, par22, par23, par24, par25, par26, par27, par28, par29, par30]

    return melty


def printMelty(melty, guessLeft):
    """
    This function prints the current state of melty
    melty- a list with all possible lines that can be drawn
    to show Melty's current state
    guessLeft: the number of guesses left before player loses
    """

    if guessLeft == 8:
        for i in range(13):
            print(melty[i])

    if guessLeft == 7:
        print(melty[5])
        for i in range(10):
            print(melty[i+3])

    if guessLeft == 6:
        print(melty[5])
        for i in range(3):
            print(melty[i+3])
        print(melty[13])
        print(melty[14])
        print(melty[15])
        print(melty[9])
        print(melty[10])
        print(melty[11])
        print(melty[12])

    if guessLeft == 5:
        print(melty[5])
        for i in range(3):
            print(melty[i+3])
        print(melty[17])
        print(melty[18])
        print(melty[19])
        print(melty[9])
        print(melty[10])
        print(melty[11])
        print(melty[12])

    if guessLeft == 4:
        print(melty[5])
        for i in range(3):
            print(melty[i+3])
        print(melty[22])
        print(melty[23])
        print(melty[24])
        print(melty[9])
        print(melty[10])
        print(melty[11])
        print(melty[12])

    if guessLeft == 3:
        print(melty[5])
        for i in range(3):
            print(melty[i+3])
        print(melty[22])
        print(melty[23])
        print(melty[24])
        print(melty[16])

    if guessLeft == 2:
        print(melty[5])
        for i in range(3):
            print(melty[i+3])

    if guessLeft == 1:
        print(melty[5])
        print(melty[28])
        print(melty[29])
        print(melty[5])

    if guessLeft == 0:
        print("    ... I've melted!  :(")


main()
