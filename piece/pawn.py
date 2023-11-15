from modi import MODI

if __name__ == "__main__":
    from piece import Piece
else:
    from piece.piece import Piece

class Pawn(Piece):

    def __init__(self, bundle: MODI, column_time: float = 1.0, degree_time: float = 1.02):
        super().__init__(bundle, column_time, degree_time)
        self.is_moved_before: bool = False

    def move(self, movement: int = 1):
        if (not self.is_moved_before):
            if (movement == 1):
                self.move_forward()
            elif (movement == 2):
                self.move_forward(2)
            self.is_moved_before = True
        else:
            self.move_forward()