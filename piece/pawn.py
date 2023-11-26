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

        self.movement: Dict[int, Dict[str, any]] = {
            1: {
                "function": lambda: self.move_forward(1),
                "expression": "한 칸 앞으로 움직입니다."
            },
            2: {
                "function": lambda: self.move_forward(1) if self.is_moved_before else self.move_forward(2) ,
                "expression": "과거에 움직이지 않은 경우, 두 칸 앞으로 움직입니다."
            }
        }

    def move(self, movement_index: int = 1):
        self.movement[movement_index]["function"]