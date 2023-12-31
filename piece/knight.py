from modi import MODI

from typing import Dict

if __name__ == "__main__":
    from piece import Piece
else:
    from piece.piece import Piece

class Knight(Piece):

    def __init__(self, bundle: MODI, column_time: float = 1.0, degree_time: float = 1.02):
        super().__init__(bundle, column_time, degree_time)
        
    def move(self, movement: int = 1):
        if (movement == 1):
            self.move_left_up(0.5)
            self.move_forward(2)
            self.move_left_up(0.5)
        elif (movement == 2):
            self.move_right_up(0.5)
            self.move_forward(1)
            self.move_right_up(0.5)
        elif (movement == 3):
            self.move_left_down(0.5)
            self.move_backward(2)
            self.move_left_down(0.5)
        elif (movement == 4):
            self.move_right_down(0.5)
            self.move_backward(2)
            self.move_right_down(0.5)
        elif (movement == 5):
            self.move_left_up(0.5)
            self.move_left(2)
            self.move_left_up(0.5)
        elif (movement == 6):
            self.move_left_down(0.5)
            self.move_left(2)
            self.move_left_down(0.5)
        elif (movement == 7):
            self.move_right_up(0.5)
            self.move_right(2)
            self.move_right_up(0.5)
        elif (movement == 8):
            self.move_right_down(0.5)
            self.move_right(2)
            self.move_right_down(0.5)