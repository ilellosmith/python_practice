# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessedWord = guessedWord + ' _ '
        else:
            guessedWord = guessedWord + letter
    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabet = string.ascii_lowercase
    alphabet_less_guessed = ''
    for letter in alphabet:
        if letter in lettersGuessed:
            alphabet_less_guessed += ''
        else:
            alphabet_less_guessed += letter
    return alphabet_less_guessed
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    # Get alphabet
    import string
    alphabet = string.ascii_lowercase

    # Intro
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %i letters long.'%len(secretWord))
    
    # Play game
    lettersGuessed = ''
    wrongGuessesLeft = 8
    while not isWordGuessed(secretWord, lettersGuessed) and wrongGuessesLeft > 0:
        
        # Echo number of guesses and available letters
        print('-------------') # separates turns
        print('You have %i guesses left'%wrongGuessesLeft)
        print('Available letters: %s'%getAvailableLetters(lettersGuessed))
        # Get user input
        guess = input('Please guess a letter: ')
        guessLowerCase = guess.lower()
        
        # QA user input
        while len(guessLowerCase)!= 1 or guessLowerCase == ' ' or guessLowerCase not in alphabet:
            if guessLowerCase == ' ':
                guess = input('It looks like you entered an empty space. Please enter a single letter from the available letters above: ')
                guessLowerCase = guess.lower()
            elif guessLowerCase not in alphabet: 
                guess = input('It looks like you entered something outside the 26 letter English alphabet. Please enter a single letter from the available letters above: ')
                guessLowerCase = guess.lower()
            else: 
                guess = input('It looks like you entered multiple letters. Please enter a single letter from the available letters above: ')
                guessLowerCase = guess.lower()
                
        # Update guesses and word
        if guessLowerCase in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: %s'
                  %getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guessLowerCase
        # Update word
            if guessLowerCase in secretWord: 
                print('Good guess: %s'%getGuessedWord(secretWord, lettersGuessed))
            else: 
                print('Oops! That letter is not in my word: %s'
                  %getGuessedWord(secretWord, lettersGuessed))
                wrongGuessesLeft -= 1
    
    # Echo results 
    print('-------------') # separates turns
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else: 
        print('Sorry, you ran out of guesses. The word was %s'%secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
