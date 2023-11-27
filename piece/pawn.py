from modi import MODI

from typing import Dict

if __name__ == "__main__":
    from piece import Piece
else:
    from piece.piece import Piece

class Pawn(Piece):

    def __init__(self, bundle: MODI, column_time: float = 1.0, degree_time: float = 1.02):
        super().__init__(bundle, column_time, degree_time)
        self.is_moved_before: bool = False

    def move(self, movement_index: int = 1):
        if (movement_index == 1):
            self.move_forward(1)
            self.is_moved_before = True
        elif (movement_index == 2):
            self.move_forward(1) if self.is_moved_before else self.move_forward(2)
            self.is_moved_before = True