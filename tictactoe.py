
from random import randint


class TicTacToe:

    def __init__(self):
        # on the grid: player is always 1 = X, and computer is 2 = O
        self._m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self._game_ended = False
        self._x_turn = True
        self._winner = -1  # -1 -> not ended, 0 -> tie, 1 -> player, 2 -> computer

    # AI will make the best move. returns [x, y]
    def play_move_ai(self):
        if self._game_ended:
            return None
        x = randint(0, 2)
        y = randint(0, 2)
        while self._m[x][y] != 0:
            x = randint(0, 2)
            y = randint(0, 2)

        self._m[x][y] = 2
        self._check_game_done()
        return [x, y]

    # This will return the probabilties of an hipotetical move. -> [wining %, tie %, lose %]
    def get_move_probability(self, player: int, x: int, y: int):
        pass

    def play_move(self, player: int, x: int, y: int) -> None:
        if self._game_ended or self._m[x][y] != 0:
            return

        self._m[x][y] = player

        self._check_game_done()

    def _check_game_done(self):
        # check for wining situations
        win = False
        winner = 0
        # checks in rows and columns
        for i in range(3):
            if self._m[0][i] == self._m[1][i] == self._m[2][i] and self._m[0][i] != 0:
                win = True
                winner = self._m[0][i]

            if self._m[i][0] == self._m[i][1] == self._m[i][2] and self._m[i][0] != 0:
                win = True
                winner = self._m[i][0]

        # checks in diagonals
        if self._m[0][0] == self._m[1][1] == self._m[2][2] and self._m[0][0] != 0:
            win = True
            winner = self._m[0][0]

        if self._m[2][0] == self._m[1][1] == self._m[0][2] and self._m[2][0] != 0:
            win = True
            winner = self._m[2][0]

        if win:
            self._winner = winner
            self._game_ended = True
            return

        # checks if grid is full
        emptycell = False
        for i in range(3):
            for j in range(3):
                if self._m[i][j] == 0:
                    emptycell = True

        if not emptycell:
            self._game_ended = True
            self._winner = 0

    def is_game_done(self) -> bool:
        return self._game_ended

    def get_winner(self) -> int:
        return self._winner

    def get_value(self, x: int, y: int) -> int:
        if x not in range(3) or y not in range(3):
            return -1
        return self._m[x][y]

    def reset(self):
        self._m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self._game_ended = False
        self._x_turn = True
        self._winner = -1


