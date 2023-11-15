from piece import Piece
from movable.movable import Movable

class Pawn(Piece, Movable):

    def __init__(self):
        self.is_moved_before: bool = False

    def move(self, move: int = 1):
        if (not self.is_moved_before):
            if (move == 1):
                self.move_forward()
            elif (move == 2):
                self.move_forward(2)
        else:
            self.move_forward()