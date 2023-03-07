from Pieces.Piece import Empty, Piece


class Movement:
    def __init__(self):
        pass

    def isAllowed(self, allowedMovements, move):
        for allowedMovement in allowedMovements:
            if (allowedMovement[0] == move[2]) and (allowedMovement[1] == move[3]):
                return True
        return False

    def dearScreen(self):
        print("########            ######  ##     ## ########  ######   ######  ")
        print("##     ##          ##    ## ##     ## ##       ##    ## ##    ## ")
        print("##     ## ##    ## ##       ##     ## ##       ##       ##       ")
        print("########   ##  ##  ##       ######### ######    ######   ######  ")
        print("##          ####   ##       ##     ## ##             ##       ## ")
        print("##           ##    ##    ## ##     ## ##       ##    ## ##    ## ")
        print("##           ##     ######  ##     ## ########  ######   ######  ")
        print("=================================================================")
        print("=================================================================")

    def isFree(self, board, x, y, mySide, fromPiece):
        if type(board.getFigure(x, y)) is Empty().__class__:
            return True
        if fromPiece.side != board.getFigure(x, y).side:
            return False
        if fromPiece.side == board.getFigure(x, y).side:
            return True
        return False

    def chooseColor(self):
        print("Hint: PyChess is still in development, so there might be any issues\n")
        print("Which color? (W/b) > ", end="")
        playerInput = input()
        print("=================================================================")
        print("=================================================================")
        return playerInput.lower() == "w"

    def inBounds(self, x, y):
        return (0 <= x < 8) and (0 <= y < 8)

    def prepare(self, movement):
        move = [letter for letter in movement]
        return [
            self.letterToNumber(move[0]) - 1,
            int(move[1]) - 1,
            self.letterToNumber(move[2]) - 1,
            int(move[3]) - 1,
        ]

    def letterToNumber(self, letter):
        return ord(letter) - 96

    def getInput(self, board):
        if board.currentSide:
            print("WHITE [From,To] > ", end="")
        else:
            print("BLACK [From,To] > ", end="")
        playerInput = input()
        return playerInput

    def move(self, board):
        playerInput = self.getInput(board)
        movement = self.prepare(playerInput)
        board.setField(movement)
        board.printBoard()
