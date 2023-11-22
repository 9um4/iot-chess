from modi import MODI

if __name__ == "__main__":
    from piece import Piece
else:
    from piece.piece import Piece

class Rook(Piece):
    
    def __init__(self, bundle: MODI, column_time: float = 1.0, degree_time: float = 1.02):
        super().__init(bundle, column_time, degree_time)
        
    def move(self, movement: int = 1):
        n = int(input("Select Distance:"))
        if (movement == 1):
            self.move_forward(n)
        elif (movement == 2):
            self.move_right(n)
        elif (movement == 3):
            self.move_backward(n)
        elif (movement == 4):
            self.move_left(n)