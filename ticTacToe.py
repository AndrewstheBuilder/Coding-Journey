theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ',
            '5': ' ', '6': ' ', '7': ' ', '8': ' ',
            '9': ' '}
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
def checkWin(turn):
    if theBoard['1'] == theBoard['2'] == theBoard['3'] == turn:
        print("\n|Player " + turn + " has won the game.|")
        return True
    if theBoard['4'] == theBoard['5'] == theBoard['6'] == turn:
        print("\n|Player " + turn + " has won the game.|")
        return True
    if theBoard['7'] == theBoard['8'] == theBoard['9'] == turn:
        print("\n|Player " + turn + " has won the game.|")
        return True
    if theBoard['1'] == theBoard['4'] == theBoard['7'] == turn:
        print("\n|Player " + turn + " has won the game.|")
        return True
    if theBoard['2'] == theBoard['5'] == theBoard['8'] == turn:
        print("\n|Player " + turn + " has won the game.|")
        return True
    if theBoard['3'] == theBoard['6'] == theBoard['9'] == turn:
        print("\n|Player " + turn + " has won the game.|")
        return True
    if theBoard['1'] == theBoard['5'] == theBoard['9'] == turn:
        print("\n|Player " + turn + " has won the game.|")
        return True
    if theBoard['5'] == theBoard['7'] == theBoard['3'] == turn:
        print("\n|Player " + turn + " has won the game.|")
        return True
    return False
turn = 'X'
for i in range(9):
    print("\n")
    printBoard(theBoard)
    print('Turn for ' + turn + ' . Move on which space?')
    move = input()
    if(theBoard[move] == ' '):
        theBoard[move] = turn
    else:
        while theBoard[move] != ' ':
            printBoard(theBoard)
            print('Enter another space! ')
            move = input()
        theBoard[move] = turn
    if checkWin(turn):
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

