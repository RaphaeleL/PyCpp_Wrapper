from Pieces.Piece import Piece, Empty
from Utils.Movement import Movement

class Queen(Piece):
    def __init__(self, side, value, representation):
        self.side = side 
        self.value = value 
        self.representation = representation

    def getAllBishopMovesA(self, move): 
        movementUtil = Movement()
        allMovements = []
        x = move[0]
        y = move[1]
        while (movementUtil.inBounds(x, y)):
            x += 1
            y += 1 
            if not [[x, y]] in allMovements: 
                allMovements.append([x, y])
        return allMovements

    def getAllBishopMovesB(self, move): 
        movementUtil = Movement()
        allMovements = []
        x = move[0]
        y = move[1]
        while (movementUtil.inBounds(x, y)):
            x -= 1
            y -= 1 
            if not [[x, y]] in allMovements: 
                allMovements.append([x, y])
        return allMovements

    def getAllBishopMovesC(self, move): 
        movementUtil = Movement()
        allMovements = []
        x = move[0]
        y = move[1]
        while (movementUtil.inBounds(x, y)):
            x += 1
            y -= 1 
            if not [[x, y]] in allMovements: 
                allMovements.append([x, y])
        return allMovements

    def getAllBishopMovesD(self, move): 
        movementUtil = Movement()
        allMovements = []
        x = move[0]
        y = move[1]
        while (movementUtil.inBounds(x, y)):
            x -= 1
            y += 1 
            if not [[x, y]] in allMovements: 
                allMovements.append([x, y])
        return allMovements

    def getAllRookMovesA(self, move): 
        movementUtil = Movement()
        allMovements = []
        x = move[0]
        y = move[1]
        while (movementUtil.inBounds(x, y)):
            x -= 1 
            if not [[x, y]] in allMovements: 
                allMovements.append([x, y])
        return allMovements

    def getAllRookMovesB(self, move): 
        movementUtil = Movement()
        allMovements = []
        x = move[0]
        y = move[1]
        while (movementUtil.inBounds(x, y)):
            x += 1 
            if not [[x, y]] in allMovements: 
                allMovements.append([x, y])
        return allMovements

    def getAllRookMovesC(self, move): 
        movementUtil = Movement()
        allMovements = []
        x = move[0]
        y = move[1]
        while (movementUtil.inBounds(x, y)):
            y -= 1 
            if not [[x, y]] in allMovements: 
                allMovements.append([x, y])
        return allMovements

    def getAllRookMovesD(self, move): 
        movementUtil = Movement()
        allMovements = []
        x = move[0]
        y = move[1]
        while (movementUtil.inBounds(x, y)):
            y += 1 
            if not [[x, y]] in allMovements: 
                allMovements.append([x, y])
        return allMovements
    
    def __str__(self): 
        return self.representation

    def checkMove(self, board, move, side):
        movementUtil = Movement()
        allowedMovements = []
        allMovements = []
        allMovements.extend(self.getAllRookMovesA(move))
        allMovements.extend(self.getAllRookMovesB(move))
        allMovements.extend(self.getAllRookMovesC(move))
        allMovements.extend(self.getAllRookMovesD(move))
        allMovements.extend(self.getAllBishopMovesA(move))
        allMovements.extend(self.getAllBishopMovesB(move))
        allMovements.extend(self.getAllBishopMovesC(move))
        allMovements.extend(self.getAllBishopMovesD(move))
        for movement in allMovements: 
            x = movement[0]
            y = movement[1]
            if movementUtil.inBounds(x, y):
                if board.getFigure(x, y) is Empty():
                    if movementUtil.isFree(board, x, y, side, board.getFigure(move[0], move[1])):
                        allowedMovements.append([x, y])
                else: 
                    if board.getFigure(x, y).side != board.getFigure(move[0], move[1]).side: 
                        allowedMovements.append([x, y])
        return movementUtil.isAllowed(allowedMovements, move)
