from board_model import *
from board_view import *


class TicTacToe:
    def __init__(self):
        self.player_letter = "X"
        self.board_model = BoardModel(3)
        self.board_view = BoardView(3, self.player_move)

    def player_move(self, move, source):
        print(move[0], move[1])
