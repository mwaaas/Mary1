import random
def guess():
    a=random.randrange(1, 1000)
    return a
def printstatement():
    print ("i have a number between 1 and 1000")
    print ("can you guess my number?")
printstatement()
y=guess()
print y

x=int(raw_input("please type your first guess:"))
while(x>=0):
    if (x<y):
        print ("Too low! Try again")
        x=int (raw_input('enter a number'))
    elif (x>y):
        print ("Too high! Try again")
        x=int (raw_input('enter a number'))
    else:
        print ("Excellent! You guessed the number")
        q=raw_input("would you like to play again (y or n)? enter y to play again or n to exit the game")
        if(q=='y'):
            printstatement()
            x=int(raw_input("please type your first guess:"))
            y=guess()
            print y
        else:
            exit()

    


 
