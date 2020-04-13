#! python3
MAX_GUESSES =10
NUM_DIGITS = 3

import random

def getSecretNum():
    num = list(range(10))
    random.shuffle(num)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(num[i])
    return secretNum

def isOnlyDigits(num):
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

def getClues(guess, s_num):
    if guess == s_num:
        return 'You got it correct'
    clues = []
    for i in range(len(guess)):
        if guess[i] == s_num[i]:
            clues.append('Rock')
        elif guess[i] in s_num:
            clues.append('Scissor')
    if len(clues) == 0:
        return 'Paper'
    clues.sort()
    return ' '.join(clues)

def playAgain():
    print('Do you want to play again (yes/no)')
    return input().lower().startswith('y')




print('Number Deduction Game')
print(f'I\'m thinking to give {NUM_DIGITS} number, try to guess')
print("When i say         what it means")
print("Paper              None of the digits is correct")
print("Scissor            One is digit is correct and in wrong position")
print("Rock               One is digit is correct and in right position")

while True:
    secretNum = getSecretNum()
    #print(secretNum)
    print(f'i have thought of number, you have {MAX_GUESSES} guess')
    guesstaken = 1
    while guesstaken <= MAX_GUESSES:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print(f'Guess {guesstaken}')
            guess = input()
        print(getClues(str(guess), str(secretNum)))
        guesstaken += 1

        if guess == secretNum:
            break
        elif guesstaken>MAX_GUESSES:
            print(f'You ran out of guess, the secret Number is {secretNum}')
    if not playAgain():
        break



