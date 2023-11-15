import modi

from piece.pawn import Pawn

import asyncio

pawn: Pawn = Pawn(bundle=modi.MODI())

command = None
while command != "quit":
    command = input("command: ")
    if (command in ["1", "2"]):
        pawn.move(int(command))

print("Program Terminated.")