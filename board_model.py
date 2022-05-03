from typing import List
from collections import Counter


def line_win(squares: List[str | None]) -> str | None:
    counts = Counter(squares)
    if 3 in counts.values():
        winner = [k for (k, v) in counts.items() if v == 3]
        return winner[0]
    return None


class BoardModel:
    def __init__(self, size=3):
        self.squares = [[None for _ in range(size)] for _ in range(size)]
        self.size = size
        self.moves = 0

    def __str__(self):
        board_str = ""
        for r in range(self.size):
            for c in range(self.size):
                board_str += self.squares[r][c] if self.squares[r][c] else "_"
            board_str += "\n"
        return board_str

    def add_move(self, row, col, value):
        if row < self.size and col < self.size:
            if self.squares[row][col]:
                raise Exception("Square already taken")
            else:
                self.squares[row][col] = value
                self.moves += 1

    def game_over(self) -> str | None:
        for r in range(self.size):
            winner = line_win(self.squares[r])
            if winner:
                return winner

        for c in range(self.size):
            winner = line_win([self.squares[r][c] for r in range(self.size)])
            if winner:
                return winner

        winner = line_win([self.squares[i][i] for i in range(self.size)])
        if winner:
            return winner

        winner = line_win([self.squares[i][self.size - i - 1] for i in range(self.size)])
        if winner:
            return winner

        if self.moves == self.size ** 2:
            return 't'  # Game ended in tie



