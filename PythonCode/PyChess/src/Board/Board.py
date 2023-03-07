from Pieces.Piece import Empty
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.Piece import Empty
from Pieces.Queen import Queen
from Pieces.Rook import Rook

class Board():
    def __init__(self, color):
        self.currentSide = color
        self.winner = False
        self.winnerSide = None
        self.board = [[], [], [], [], [], [], [], []]
        self.fillBoard()
        self.printBoard()

    def isWinner(self):
        return self.winner

    def setWinner(self, winner):
        self.winner = winner

    def handleWinner(self):
        print("==========================================================")
        print("==========================================================")
        if self.winnerSide:
            print("White won")
        elif not self.winnerSide:
            print("Black won")
        print("==========================================================")
        print("==========================================================")

    def checkWinner(self):
        blackCount, whiteCount = 0, 0
        for tmp in self.board:
            for piece in tmp:
                if not type(piece) is Empty().__class__:
                    if piece.side:
                        whiteCount += 1
                    else:
                        blackCount += 1
        if blackCount == 0:
            self.setWinner(True)
            self.winnerSide = False
        elif whiteCount == 0:
            self.setWinner(False)
            self.winnerSide = True

    def setFigure(self, x, y, figure):
        self.board[x][y] = figure

    def getFigure(self, x, y):
        return self.board[x][y]

    def setField(self, move):
        toMove = self.getFigure(move[1], move[0])
        if toMove.checkMove(self, [move[1], move[0], move[3], move[2]], self.currentSide):
            self.setFigure(move[1], move[0], Empty())
            self.setFigure(move[3], move[2], toMove)
        else:
            print("Move is not allowed. Try again!".upper())
            self.currentSide = not self.currentSide

    def fillBoard(self):
        self.board[0].append(Rook(True, 5, "R"))
        self.board[0].append(Knight(True, 3, "K"))
        self.board[0].append(Bishop(True, 3, "B"))
        self.board[0].append(Queen(True, 9, "Q"))
        self.board[0].append(King(True, 0, "X"))
        self.board[0].append(Bishop(True, 3, "B"))
        self.board[0].append(Knight(True, 3, "K"))
        self.board[0].append(Rook(True, 5, "R"))
        for _ in range(8):
            self.board[1].append(Pawn(True, 1, "P"))
            for i in range(2, 6):
                self.board[i].append(Empty())
            self.board[6].append(Pawn(False, 1, "p"))
        self.board[7].append(Rook(False, 5, "r"))
        self.board[7].append(Knight(False, 3, "k"))
        self.board[7].append(Bishop(False, 3, "b"))
        self.board[7].append(King(False, 0, "x"))
        self.board[7].append(Queen(False, 9, "q"))
        self.board[7].append(Bishop(False, 3, "b"))
        self.board[7].append(Knight(False, 3, "k"))
        self.board[7].append(Rook(False, 5, "r"))

    def printBoard(self):

        print("+-------------+")
        print("| Black       |")
        print("+-------------+")
        print("\na1                     h1")
        print("   +-----------------+")
        for tmp in self.board:
            print("   | ", end="")
            for piece in tmp:
                print(str(piece) + " ", end="")
            print("| ", end="")
            print()
        print("   +-----------------+")
        print("a8                     h8\n")
        print("\t\t\t+-------------+")
        print("\t\t\t| White       |")
        print("\t\t\t+-------------+\n")


