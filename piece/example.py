if __name__ == "__main__":
    from piece import Piece
else:
    from piece.piece import Piece


class Example_Piece(Piece):

    def move(self, movement: int = 1):
        if (movement == 1):
            self.move_forward()