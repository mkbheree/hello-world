#! python3
import random

HANGMAN_PICS = ['''
    +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
      ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0,len(words)-1)
    return wordList[wordIndex]

def displayBoard(missedltr,correctltr,secretword):
    print(HANGMAN_PICS[len(missedltr)])
    print()
    print("Missed Letters", end=' ')
    for ltr in missedltr:
        print(ltr)
    print()
    blanks = '_'*len(secretword)
    for i in range(len(secretword)):
        if secretword[i] in correctltr:
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]
    for b in blanks:
        print("Letter: ", b)
    print()

def getGuessedLetter(completeGuess):
    guess = input('Please enter a letter')
    guess = guess.lower()
    if len(guess)!=1:
        print('please enter single letter')
    elif guess in completeGuess:
        print('You have already choose this letter,try another')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('Enter correct character')
    else:
        return guess

def playAgain():
    print("Do you want to play again(Yes/No)")
    return input().lower().startswith('y')



print("H    A   N   G   M   A   N")
gameIsDone = False
missedLetters = ' '
correctLetters = ' '
secretWord = getRandomWord(words)

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuessedLetter(missedLetters+correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! you have won, the Secret Word is '+secretWord.upper())
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICS)-1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print("you are out of chances.GAME OVER")
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            gameIsDone = False
            missedLetters = ' '
            correctLetters = ' '
            secretWord = getRandomWord(words)
        else:
            break



