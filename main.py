import modi

from system.game import Game

from piece.pawn import Pawn
from piece.knight import Knight

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

player_index: int = game.register_player(nickname, piece_index, 0, 0) != -1

print(player_index)

if (player_index != -1):
    piece = Knight(modi.MODI())
    while piece.__is_alive__:
        state = game.spread_reader.get_state(player_index)
        if state == "MY_TURN":
            if (piece.__display__.text != "My turn!"):
                piece.__display__.text = "My turn!"
            command = game.spread_reader.
            if (command != 0):
                piece.move(int(command))
                game.spread_reader.set_command(player_index, None)
                game.spread_reader.set_state(player_index, "OPPONENT_TURN")
                game.spread_reader.set_state(3 - player_index, "MY_TURN")
            sleep(2)

        elif state == "OPPONENT_TURN":
            if (piece.__display__.text != "Opponent's turn!"):
                piece.__display__.text = "Opponent's turn!"
            for _ in range(0, 200):
                sleep(0.01)
                piece.__detect_die__()

        else:
            if (piece.__display__.text != "Waiting for other player..."):
                piece.__display__.text = "Waiting for other player..."
            sleep(2)

else:
    print("게임을 실행할 수 없습니다!")

print("Program Terminated.")