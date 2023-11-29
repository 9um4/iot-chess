import modi

from system.game import Game

from piece.piece import Piece
from piece.pawn import Pawn
from piece.knight import Knight
from piece.rook import Rook

from time import sleep

game: Game = Game()

nickname = None

while (not nickname):
    print("이번 게임에 사용할 닉네임을 입력해 주세요.")
    nickname = input()

piece_index: int = 0

while (not piece_index):
    print("이번 게임에 사용할 말을 정해 주세요.")
    piece_index = int(input())

piece: Piece = None
if piece_index == 1:
    piece = Knight(modi.MODI())
elif piece_index == 2:
    piece = Pawn(modi.MODI())
elif piece_index == 3:
    piece = Rook(modi.MODI())

player_index: int = game.register_player(nickname, piece_index, 0, 0)

while piece.__is_alive__ and player_index != -1:
    if (player_index == 1):
        if (game.spread_reader.first_player['state'] == "MY_TURN"):
            if (piece.__display__.text != "My turn!"):
                piece.__display__.text = "My turn!"
            command = game.spread_reader.first_player['command']
            if (command != 0):
                piece.move(command)
                game.spread_reader.first_player['command'] = 0
                game.spread_reader.first_player['state'] = "OPPONENT_TURN"
                game.spread_reader.second_player['state'] = "MY_TURN"
            sleep(2)
        elif (game.spread_reader.first_player['state'] == "OPPONENT_TURN"):
            if (piece.__display__.text != "Opponent turn!"):
                piece.__display__.text = "Opponent turn!"
            for _ in range(0, 20):
                piece.__detect_die__()
                sleep(0.1)
        else:
            if (piece.__display__.text != "Waiting for other player..."):
                piece.__display__.text = "Waiting for other player..."
        sleep(2)
    elif (player_index == 2):
        if (game.spread_reader.second_player['state'] == "MY_TURN"):
            if (piece.__display__.text != "My turn!"):
                piece.__display__.text = "My turn!"
            command = game.spread_reader.second_player['command']
            if (command != 0):
                piece.move(command)
                game.spread_reader.second_player['command'] = 0
                game.spread_reader.second_player['state'] = "OPPONENT_TURN"
                game.spread_reader.first_player['state'] = "MY_TURN"
            sleep(2)
        elif (game.spread_reader.second_player['state'] == "OPPONENT_TURN"):
            if (piece.__display__.text != "Opponent turn!"):
                piece.__display__.text = "Opponent turn!"
            for _ in range(0, 20):
                piece.__detect_die__()
                sleep(0.1)
        else:
            if (piece.__display__.text != "Waiting for other player..."):
                piece.__display__.text = "Waiting for other player..."

if (player_index == -1):
    print("게임을 실행할 수 없습니다!")

print("Program Terminated.")