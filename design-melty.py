"""
This program is analogous to Hangman. User keeps guess the word
With every wrong attempt a snowman melts till user runs out of attempts.
Names: Elijah Cavalier, Andrew Henin
Date: March 2022
"""

def main():

    #this creates a list with the length of the imported word.
    answerList = wordGen()
    correctList = ["-"]*len(answerList)
    guessList = []
    melty = drawMelty()
    guessLeft = 8
    welcome()

    while not gameOver(guessLeft, correctList):
        printMelty(melty)
        #This prints Melty's current state
        printGame(guessLeft, correctList)
        #It includes the incomplete/complete word and how many attempts remaining
        guess = inputGuess(correctList, guessList)
        #It gets an input and checks for it if it’s valid
        guessList.append(guess)
        #this appends any guess in the list to keep track of all guesses
        if checkGuess(guess, correctList, answerList) == False:
                #For loop to check for the letter in the word and prints if the ch is in or not
                #It also prints out a statement if the ch is in word
                guessLeft = guessLeft - 1
                meltMelty(melty)
                #This changes Melty's state

    printOutMsg(correctList)
    # it calls check if won or loss which prints th()e final msg either loss or win


def welcome():
    """
    This function prints the welcome message.
    """
    print("inside welcome()")


def wordGen():
    """
    This function reads the words file
    It generates a random word from it
    returns: a list of characters answerList = [ch’s in word]
    """
    answerList = [""]
    print("inside wordGen()", answerList)

    return answerList



def meltMelty(melty):
    """
    This function changes Melty's current state
    It just edits the list in main
    melty is a list of melty's components
    """
    print("inside meltMelty")



def printMelty(melty):
    """
    This function prints Melty's current state
    It takes Melty's drawing list
    melty is a list of melty's components
    """

    print("inside printMelty()")



def printGame(guessLeft, correctList):- Elijah and Andrew
    """
    It prints the updated guess.
    It also includes how many attempts remaining
    guessLeft is the number of remaining guesses
    correctList is a list of the correct guessed characters of the word
    """

    print("inside printGame()")


def inputGuess(correctList, guessList):
    """
    It gets an input and checks for it if it’s repeated
    correctList is a list of the correct guessed char- Elijah and Andrewacters of the word
    guessList is the list of all guess characters whether right or wrong
    """

    guess = ""
    print("inside inputGuess()", guess)

    return guess


def checkGuess(guess, correctList, answerList):
    """
    It contains a for loop to check for the letter in the word
    and prints if the ch is in word or not
    guess is the guessed character
    correctList is a list of the correct guessed characters of the word
    answerList is the list of tyhe characters of the answer word
    returns a boolean value True or False depending on whether the guessis correct
    """
    print("inside checkGuess")

    return True #or False


def gameOver(guessLeft, correctList):
    """
    This function checks if game is over.
    guessLeft is the number of remaining guesses
    correctList is a list of the correct guessed characters of the word
    returns boolean value True or False
    """

    print("inside gameOver()")

    return True #or False

def printOutMsg(correctList):
    """
    This function calls winOrLoss
    and prints the final msg
    correctList is a list of the correct guessed characters of the word
    """

    if winOrLoss(correctList) == True:
        print("win")
    else:
        print("loss")

    print("inside printOutMsg()")


def winOrLoss(correctList):
    """
    correctList is a list of the correct guessed characters of the word
    returns True or False (win or loss)
    """

    print("inside winOrLoss()")

    return True #or False


def drawMelty():
    """
    This function has the components of Melty
    It draws Melty as a list and returns it to main()
    returns Melty
    """

    melty = []
    print("inside drawMelty()", melty)

    return melty


main()
