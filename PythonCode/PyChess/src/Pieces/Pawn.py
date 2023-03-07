from Pieces.Piece import Piece
from Utils.Movement import Movement

class Pawn(Piece):
    def __init__(self, side, value, representation):
        self.side = side 
        self.value = value 
        self.representation = representation
    
    def __str__(self): 
        return self.representation

    def checkMove(self, board, move, side):
        movementUtil = Movement()
        allowedMovements = []
        allowedKeys = [[1, 0], [1, 1], [1, -1]]
        baseline = 6 if side else 1 
        for allowedKey in allowedKeys:
            if move[0] == baseline:
                allowedMovements.append([move[0]-2 if side else move[0]+2, move[1]])
            x = move[0] - allowedKey[0] if side else move[0] + allowedKey[0]
            y = move[1] - allowedKey[1] if side else move[1] + allowedKey[1]
            if movementUtil.inBounds(x, y):
                if move[1] != y:
                    if not movementUtil.isFree(board, x, y, side, board.getFigure(move[0], move[1])):
                        allowedMovements.append([x, y])
                else:
                    allowedMovements.append([x, y])
        return movementUtil.isAllowed(allowedMovements, move)