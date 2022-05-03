from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from tic_tac_toe import *


class GameApp(App):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def build(self):
        sm = ScreenManager()
        sm.add_widget(self.game_view)
        return sm


def main():
    # board = BoardModel()
    # board.add_move(1, 1,'x')
    # board.add_move(2, 0, 'x')
    # board.add_move(0, 2, 'x')
    #
    # print(board)
    # print(board.game_over())

    game = TicTacToe()
    GameApp(game.board_view).run()


if __name__ == '__main__':
    main()
