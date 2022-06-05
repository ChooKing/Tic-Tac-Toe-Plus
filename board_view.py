from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial


class BoardView(Screen):
    def __init__(self, size, callback):
        super().__init__()
        self.buttons = []
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text="Tic Tac Toe Plus", font_size='40sp', size_hint=(1, 0.1)))
        grid = GridLayout()
        grid.cols = size
        for r in range(size):
            row = []
            for c in range(size):
                button = Button(text="", font_size='120sp')
                button.bind(on_press=partial(callback, (r, c)))
                row.append(button)
                grid.add_widget(button)
            self.buttons.append(row)
        box.add_widget(grid)
        self.add_widget(box)

    def set_cell(self, row, col, val):
        self.buttons[row][col].text = val
