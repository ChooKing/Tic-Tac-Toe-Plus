from typing import List, Tuple, Set
from collections import Counter
from enum import Enum
import random

class Players(Enum):
    X = 'X'
    O = 'O'
    TIE = 'TIE'


class BoardModel:
    def __init__(self, size=3):
        self.squares = [[None for _ in range(size)] for _ in range(size)]
        self.size = size
        self.moves = 0
        self.winner: Players | None = None
        self.available: Set[Tuple[int, int]] = set()
        for r in range(size):
            for c in range(size):
                self.available.add((r, c))

    def __str__(self):
        board_str = ""
        for r in range(self.size):
            for c in range(self.size):
                board_str += self.squares[r][c] if self.squares[r][c] else "_"
            board_str += "\n"
        return board_str

    def add_move(self, row: int, col: int, value: str | None):
        if row < self.size and col < self.size:
            if self.squares[row][col]:
                pass
                #raise Exception("Square already taken")
            else:
                self.squares[row][col] = value
                self.available.remove((row, col))
                self.moves += 1

    def line_count(self, squares: List[str | None]) -> Tuple[Tuple[str | None, int], bool]:
        counts = Counter(squares)
        most_common = counts.most_common(1)[0]
        if most_common[1] == self.size and most_common[0]:
            self.winner = Players.O if most_common[0] == 'O' else Players.X

        return most_common, len(counts) == 2 and counts[None] > 0

    def get_filler(self, line: List[Tuple[int, int]]) -> Tuple[int, int]:
        empties = []
        for square in line:
            if not self.squares[square[0]][square[1]]:
                empties.append(square)
        return random.choice(empties)

    def get_move(self) -> Tuple[int, int] | None:
        """Decide next move for computer"""
        """IF HALF OR MORE HUMAN PLAYER'S LETTER IN A COLUMN, ROW, OR DIAGONAL, ADD SOMETHING"""
        losers: List[List[Tuple[int, int]]] = []   # List of sequences oen move away from losing
        wins: List[List[Tuple[int, int]]] = []  # List of sequences one move away from winning
        over_half : List[List[Tuple[int, int]]] = []  # Sequences in which more than half are the same letter and the rest are empty

        def categorize(leader: Tuple[Tuple[str, int], bool], line: List[Tuple[int, int]]):
            if leader[0][1] == self.size - 1:
                if leader[0][0] and leader[1]:
                    if leader[0][0] == 'O':
                        wins.append(line)
                    else:
                        losers.append(line)
            elif leader[1] and leader[0][0] and leader[0][1] > self.size // 2:
                over_half.append(line)

        for r in range(self.size):
            lead = self.line_count(self.squares[r])
            coords = [(r, c) for c in range(self.size)]
            categorize(lead, coords)

        for c in range(self.size):
            col = [self.squares[r][c] for r in range(self.size)]
            coords = [(r, c) for r in range(self.size)]
            lead = self.line_count(col)
            categorize(lead, coords)

        coords = [(i, i) for i in range(self.size)]
        diag1 = [self.squares[i][i] for i in range(self.size)]
        lead = self.line_count(diag1)
        categorize(lead, coords)

        coords = [(i, self.size - i -1) for i in range(self.size)]
        diag2 = [self.squares[i][self.size - i - 1] for i in range(self.size)]
        lead = self.line_count(diag2)
        categorize(lead, coords)
        if self.moves == self.size ** 2:
            self.winner = Players.TIE
            return None

        if wins:
            return self.get_filler(wins[0])
        if losers:
            print("Need block?")
            return self.get_filler(losers[0])
        if over_half:
            return self.get_filler(over_half[0])

        return random.choice(list(self.available))



