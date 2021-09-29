class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.board = self.setBoard()
        self.lastPlayer = ''

    def setBoard(self):
        i = self.i
        j = self.j
        board = [['O' for x in range(i)] for y in range(j)]
        return board

    def getBoard(self):
        return self.board

    def printBoard(self):
        i = 0
        while i < len(self.board):
            print(self.board[i])
            i = i + 1
        return self

    def getLastPlayer(self):
        return self.lastPlayer

    def setLastPlayer(self, player):
        self.lastPlayer = player
        return self

    def play(self, y, player):
        y = int(y)

        if player == self.lastPlayer:
            print('Vous avez déja jouer')
            player2 = input('Entrez votre couleur: ')
            y2 = input('Choisissez votre colonne: ')
            self.play(y2, player2)

        i = len(self.board) - 1
        while i >= 0:
            # check every i on y axis and drop token lowest possible
            if self.board[i][y] == 'O':
                self.board[i][y] = player
                break
            i = i - 1

        self.setLastPlayer(player)
        self.printBoard()

        player2 = input('Entrez votre couleur: ')
        if player2 not in ['R', 'J']:
            player2 = input('Veuillez choisir R ou J: ')

        y2 = input('Choisissez votre colonne: ')
        if y2 not in range(0, len(self.board) - 1):
            y2 = input('Choisissez une colonne entre 0 et ' + str(len(self.board)) + ': ')

        self.play(y2, player2)


game = Board(5, 5)
game.play(0, 'J')
