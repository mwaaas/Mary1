# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
def hangman():
    y=random.choice(wordlist)
    print "welcome to the game, hangman!"
    print "i am thinking of a word that is", len(y),"letters long"
    print "length is",len(y)
    return y

    

def guess():
    y=hangman()
    print "You have", 2*len(y), "guesses left."
    letters = ["abcdefghijklmnopqrstuvwxyz"]
    #print letters[2]
    print "Available letters:",
    for i in letters:
        print i
        print "new y is:", y
    for i in range (len(y)):
        
        l=raw_input("please enter a number")
    
        result= ['-'*(len(y))]
        #if(l in random.choice(wordlist)):
        #print random.choice(wordlist))):
        if(l in y):
            print "Good guess:",
            for i in result:
                #result.insert(l)
                print i
                #if(l==i):
                    #letters.remove(l)
                    #print i
                
        else:
            print "Oops! That letter is not in my word:",
            for i in result:
                print i
                
        print "new y is:", y
guess()
"""code to put append the letter if it's a good guess  to afta goodguess in the same position the letter
is in the randomly selected word. and also code to delete the letter typed from the list of available letters."""

