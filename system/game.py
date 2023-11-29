from system.spread_reader import Spread_Reader

from piece.piece import Piece

from random import randint

class Game:
    def __init__(self) -> None:
        self.spread_reader: Spread_Reader = Spread_Reader("./.credentials/key.json")
    
    def register_player(
            self,
            name: str,
            piece: Piece,
            location_x: int,
            location_y: int
            ) -> int:
        if (not self.spread_reader.player_exists(1)):
            self.spread_reader.first_player['id'] = randint(10000000, 99999999)
            self.spread_reader.first_player['name'] = name
            self.spread_reader.first_player['state'] = "IDLE"
            self.spread_reader.first_player['piece'] = piece
            self.spread_reader.first_player['location_x'] = 1
            self.spread_reader.first_player['location_y'] = 3
            self.spread_reader.first_player['command'] = 0
            self.spread_reader.update_first_player()
            return 1
        elif (not self.spread_reader.player_exists(2)):
            self.spread_reader.second_player['id'] = randint(10000000, 99999999)
            self.spread_reader.second_player['name'] = name
            self.spread_reader.second_player['state'] = "OPPONENT_TURN"
            self.spread_reader.second_player['piece'] = piece
            self.spread_reader.second_player['location_x'] = 2
            self.spread_reader.second_player['location_y'] = 1
            self.spread_reader.second_player['command'] = 0
            self.spread_reader.update_second_player()
            self.spread_reader.first_player['state'] = 'MY_TURN'
            self.spread_reader.update_first_player()
            return 2
        else:
            return -1