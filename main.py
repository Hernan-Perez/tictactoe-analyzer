import tkinter as tk
import tkinter.messagebox

import tictactoe as tc


class TicTacToeWindow:

    def __init__(self):
        self.analysis_mode = False
        self.ttt = tc.TicTacToe()
        self.player = 1
        self.win = None
        self.btns = []
        self.btn_toggle = None
        self.lbl_res = None
        self.img_empty = self.img_cross = self.img_circle = None

    def toggle_action(self):

        self.analysis_mode = not self.analysis_mode

        if self.analysis_mode:
            self.btn_toggle.config(text="Change to play mode")
            self.lbl_res.config(text="Press an empty square to see the probabilities")
        else:
            self.btn_toggle.config(text="Change to analysis mode")
            self.lbl_res.config(text="")

    def ttt_button_pressed(self, x: int, y: int) -> None:
        if self.ttt.get_value(x, y) != 0 or self.ttt.is_game_done():
            return

        if self.analysis_mode:
            prob = self.ttt.get_move_probability(self.player, x, y)
        else:
            # player's action
            self.ttt.play_move(self.player, x, y)
            self.btns[x + y * 3].config(image=self.img_cross)

            # computer's action
            res = self.ttt.play_move_ai()
            if res is not None:
                self.btns[res[0] + res[1] * 3].config(image=self.img_circle)

            if self.ttt.is_game_done():
                txt = ""
                winner = self.ttt.get_winner()

                if winner == 0:
                    txt = "Game ended with a tie."
                if winner == 1:
                    txt = "You won."
                if winner == 2:
                    txt = "You lost."

                tkinter.messagebox.showinfo("Game ended", txt)

    def show_window(self):
        self.win = tk.Tk()
        self.win.title("Tic Tac Toe Analyzer")
        self.win.geometry("700x450")

        lbl = tk.Label(self.win, text="You play as X:", font="calibri 20", padx=25, pady=5)
        lbl.grid(row=0, column=0, columnspan=4)

        emptyspace = tk.Label(self.win, padx=20)
        emptyspace.grid(row=0, column=0)

        self.img_empty = tk.PhotoImage(file="img/placeholder.png")
        self.img_cross = tk.PhotoImage(file="img/cross.png")
        self.img_circle = tk.PhotoImage(file="img/circle.png")

        ww = 100
        hh = 100
        px = py = 0

        # this is a fix for self.btns:
        callback = lambda a, b: lambda: self.ttt_button_pressed(a, b)
        # if I assign command=self.ttt_button_pressed(i, j)
        # instead of callback(i, j), the assigned function is going to have a reference to i, j
        # intead of the current int values
        for j in range(3):
            for i in range(3):
                btn_aux = tk.Button(self.win, image=self.img_empty, width=ww, height=hh,
                                    command=callback(i, j))
                btn_aux.grid(row=i + 1, column=j + 1, padx=px, pady=py)
                self.btns.append(btn_aux)

        self.btn_toggle = tk.Button(self.win, text="Change to analysis mode", width=30, height=2,
                                    command=self.toggle_action)
        self.btn_toggle.grid(row=1, column=4, padx=(50, 0), pady=5)

        self.lbl_res = tk.Label(self.win, text="", width=50, height=5)
        self.lbl_res.grid(row=2, column=4, columnspan=2, padx=(0, 0), pady=0)

        btn_exit = tk.Button(self.win, text="Exit", width=10, height=2, command=exit)
        btn_exit.grid(row=4, column=1, columnspan=1, padx=5, pady=25)

        self.win.mainloop()


if __name__ == '__main__':
    w = TicTacToeWindow()
    w.show_window()
