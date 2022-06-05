from board_model import *
from board_view import *


class TicTacToe:
    def __init__(self, size):
        self.player_letter = "X"
        self.computer_letter = "O"
        self.size = size
        self.board_model = BoardModel(size)
        self.board_view = BoardView(size, self.player_move)

    def player_move(self, move, source):
        row, col = move
        self.board_model.add_move(row, col, self.player_letter)
        self.board_view.set_cell(row, col, self.player_letter)
        move = self.board_model.get_move()
        if move:
            self.board_model.add_move(move[0], move[1], self.computer_letter)
            self.board_view.set_cell(move[0], move[1], self.computer_letter)
        if self.board_model.winner:
            if self.board_model.winner != Players.TIE:
                print("Winner is: ", self.board_model.winner.value)
            else:
                print("The game ended in a tie")