from piece import Piece
from movable.movable import Movable

class Example_Piece(Piece, Movable):

    def move(self, move: int = 1):
        if (move == 1):
            self.move_forward()