def defineX(d, posX):
    if posX == d:
        posX = 1
    elif posX == d - 1:
        posX = 0
    else:
        posX += 2
    return posX


def placeQueen(board, posY, posX):
    d = len(board)
    board[posY][posX] = "X"
    posX = defineX(d, posX)
    posY += 1

    if posX == d or posY == d:
        return printBoard(board)

    return placeQueen(board, posY, posX)


def printBoard(board):
    i = 0
    while i < len(board):
        print(board[i])
        i += 1


n = int(input('i: '))
board = [['O' for x in range(n)] for y in range(n)]

if n > 3 and n % 3 == 0:
    placeQueen(board, 0, 1)
elif n > 3 and n % 2 != 0:
    placeQueen(board, 0, 0)
else:
    print('operation impossible')
