import numpy


class Board:
    def __init__(self, i, j):
        self.y = i
        self.x = j
        self.board = self.setBoard()
        self.lastPlayer = ''
        self.lastPlayerPosition = None
        self.cashPrize = "100000€"

    def setLastPlayerPosition(self, pos):
        self.lastPlayerPosition = pos
        return self

    def getLastPlayerPosition(self):
        return self.lastPlayerPosition

    def setBoard(self):
        return [['O' for x in range(self.y)] for y in range(self.x)]

    def getBoard(self):
        return self.board

    def printBoard(self):
        i = 0
        while i < len(self.getBoard()):
            print(self.getBoard()[i])
            i = i + 1
        return self

    def getLastPlayer(self):
        return self.lastPlayer

    def setLastPlayer(self, player):
        self.lastPlayer = player
        return self

    def yCheck(self, x):
        data = []
        for y in range(0, len(self.getBoard())):
            try:
                data.append(self.getBoard()[y][x])
            except IndexError:
                return data

        return data

    def xCheck(self, y):
        data = []
        for x in range(len(self.getBoard()[0])):
            try:
                data.append(self.getBoard()[y][x])
            except IndexError:
                return data

        return data

    def seCheck(self, y, x):
        seVal = []
        x += 1
        while y > 0:
            y -= 1
            x -= 1
        seOrigin = [y, x]
        try:
            while seOrigin[0] < len(self.getBoard()):
                seVal.append(self.getBoard()[seOrigin[0]][seOrigin[1]])
                seOrigin[0] += 1
                seOrigin[1] += 1
        except IndexError:
            return seVal
        return seVal

    def neCheck(self, y, x):
        flipedBoard = numpy.flip(self.getBoard(), 1)
        seVal = []
        x -= 1
        while y > 0:
            y -= 1
            x -= 1
        seOrigin = [y, x]
        try:
            while seOrigin[0] < len(self.getBoard()):
                seVal.append(flipedBoard[seOrigin[0]][seOrigin[1]])
                seOrigin[0] += 1
                seOrigin[1] += 1
        except IndexError:
            return seVal
        return seVal

    def isWon(self):
        y = self.getLastPlayerPosition()[0] - 1  # i
        x = self.getLastPlayerPosition()[1] + 1  # j
        yVal = self.yCheck(y)
        xVal = self.xCheck(x)
        seVal = self.seCheck(x, y)
        neVal = self.neCheck(x, y)

        if 'JJJJ' in ''.join(xVal) or 'JJJJ' in ''.join(yVal) or 'JJJJ' in ''.join(seVal) or 'JJJJ' in ''.join(neVal):
            return True

        if 'RRRR' in ''.join(xVal) or 'RRRR' in ''.join(yVal) or 'RRRR' in ''.join(seVal) or 'JJJJ' in ''.join(neVal):
            return True

        return False

    def getCashPrize(self):
        return self.cashPrize

    def printWinner(self):
        return print('Joueur', self.lastPlayer, 'gagne la partie et remporte', self.getCashPrize())

    def play(self, x, player):
        x = int(x)

        if player == self.lastPlayer:
            print('Vous avez déja jouer')
            player2 = input('Entrez votre couleur: ')
            y2 = input('Choisissez votre colonne: ')
            self.play(y2, player2)

        i = len(self.board) - 1
        while i >= 0:
            # check every i on y axis and drop token lowest possible
            if self.board[i][x] == 'O':
                self.board[i][x] = player
                self.setLastPlayerPosition([i, x])
                break
            i -= 1

        # victory condition
        if self.lastPlayerPosition is not None:
            if self.isWon():
                self.printBoard()
                return self.printWinner()
        self.printBoard()

        player2 = input('Entrez votre couleur: ')
        if player2 not in ['R', 'J']:
            player2 = input('Veuillez choisir R ou J: ')

        y2 = input('Choisissez votre colonne: ')

        print(len(self.getBoard()[0]) - 1)
        if int(y2) not in range(0, len(self.getBoard()[0]) - 1):
            y2 = input('Choisissez une colonne entre 0 et ' + str(len(self.board)) + ': ')

        self.play(y2, player2)


game = Board(7, 5)
game.play(0, 'J')
