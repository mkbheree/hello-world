import random
def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        letter = input("Enter your choice(X/O)")
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("what is your next move(1 to 9)")
        move = input()
        return int(move)

def isSpaceFree(board,move):
    return board[move] == ' '

def makeMove(board,move,letter):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le) )

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

def getCopyBoard(board):
    dummies = []
    for i in board:
        dummies.append(i)
    return dummies

def randomComputerMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

def getComputerMove(board,computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 10):
        copy = getCopyBoard(board)
        if isSpaceFree(copy, i):
            makeMove(copy, i, computerLetter)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1, 10):
        copy = getCopyBoard(board)
        if isSpaceFree(copy, i):
            makeMove(copy, i, playerLetter)
            if isWinner(copy, playerLetter):
                return i
    move = randomComputerMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board,5):
        return 5

    return randomComputerMoveFromList(board, [2, 4, 6, 8])





print("Welcome To TicTacToe Game")
while True:
    theBoard = [' ']*10
    playerLetter,computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("it's " + turn + " turn")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,move,playerLetter)
            if isWinner(theBoard,playerLetter):
                drawBoard(theBoard)
                print("hooray you're the Winner")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('the game is tie')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard,move,computerLetter)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('You Loose')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('the game is tie')
                    break
                else:
                    turn = 'player'




