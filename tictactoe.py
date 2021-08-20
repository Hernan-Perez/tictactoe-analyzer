
from random import randint
from copy import deepcopy
from collections import Counter


class TicTacToe:

    def __init__(self):
        # on the grid: player is always 1 = X, and computer is 2 = O
        self._m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self._game_ended = False
        self._x_turn = True
        self._winner = -1  # -1 -> not ended, 0 -> tie, 1 -> player, 2 -> computer

    # AI will make the best move in hard mode and a random move otherwise. returns [x, y]
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

    # This will return the probabilties of an hypotetical move. -> [wining %, tie %, lose %]
    def get_move_probability(self, player: int, x: int, y: int):
        if self._game_ended:
            return [0.0, 0.0, 0.0]

        listaux = deepcopy(self._m)
        listaux[x][y] = player
        r = TicTacToe._check_winner(listaux)
        if r != -1:
            if r == 0:
                return [0.0, 1.0, 0.0]
            if r == 1:
                return [1.0, 0.0, 0.0]
            if r == 2:
                return [0.0, 0.0, 1.0]
        res = TicTacToe._hypotetical_moves(listaux, player+1)
        c = Counter(res)
        total = len(res)
        total = float(total)
        return [c[1]/total, c[0]/total, c[2]/total]

    @staticmethod
    def _hypotetical_moves(grid, player: int) -> list:
        lst = []
        if player > 2:
            player = 1
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    grid[i][j] = player
                    r = TicTacToe._check_winner(grid)
                    # if its not -1 it means there is a winner or that the grid is full
                    # if its -1 its going to call itself to try the sub moves
                    if r != -1:
                        lst.append(r)
                    else:
                        lst.extend(TicTacToe._hypotetical_moves(deepcopy(grid), player + 1))

                    # clears the grid change, to test the next posibility
                    grid[i][j] = 0
        return lst

    @staticmethod
    def _is_grid_full(grid) -> bool:
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    return False

        return True

    def play_move(self, player: int, x: int, y: int) -> None:
        if self._game_ended or self._m[x][y] != 0:
            return

        self._m[x][y] = player
        self._check_game_done()

    def _check_game_done(self) -> None:
        r = TicTacToe._check_winner(self._m)
        if r != -1:
            self._winner = r
            self._game_ended = True

    @staticmethod
    def _check_winner(m) -> int:
        # check for wining situations
        win = False
        winner = -1
        # checks in rows and columns
        for i in range(3):
            if m[0][i] == m[1][i] == m[2][i] and m[0][i] != 0:
                win = True
                winner = m[0][i]

            if m[i][0] == m[i][1] == m[i][2] and m[i][0] != 0:
                win = True
                winner = m[i][0]

        # checks in diagonals
        if m[0][0] == m[1][1] == m[2][2] and m[0][0] != 0:
            win = True
            winner = m[0][0]

        if m[2][0] == m[1][1] == m[0][2] and m[2][0] != 0:
            win = True
            winner = m[2][0]

        if win:
            return winner

        if TicTacToe._is_grid_full(m):
            return 0
        return winner  # =-1

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

    def debug_print(self):
        print(self._m)
