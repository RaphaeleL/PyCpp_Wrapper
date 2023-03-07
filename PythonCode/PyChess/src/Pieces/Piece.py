class Piece(object): 
    def __init__(self, side, value, representation):
        self.side = side
        self.value = value
        self.representation = representation
    
    def __str__(self): 
        return self.representation

class Empty(Piece): 
    def __init__(self):
        self.side = None 
        self.value = -1
        self.representation = "-"
    
    def __str__(self): 
        return self.representation
