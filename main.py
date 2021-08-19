import tkinter as tk


def show_window():
    ventana = tk.Tk()
    ventana.title("Tic Tac Toe Analyzer")
    ventana.geometry("800x600")

    lbl = tk.Label(ventana, text="You play as X:", font="calibri 20", padx=25, pady=5)
    lbl.grid(row=0, column=0, columnspan=4)

    emptyspace = tk.Label(ventana, padx=20)
    emptyspace.grid(row=0, column=0)

    ww = 10
    hh = 5
    btn11 = tk.Button(ventana, text="", width=ww, height=hh)
    btn12 = tk.Button(ventana, text="", width=ww, height=hh)
    btn13 = tk.Button(ventana, text="", width=ww, height=hh)
    btn21 = tk.Button(ventana, text="", width=ww, height=hh)
    btn22 = tk.Button(ventana, text="", width=ww, height=hh)
    btn23 = tk.Button(ventana, text="", width=ww, height=hh)
    btn31 = tk.Button(ventana, text="", width=ww, height=hh)
    btn32 = tk.Button(ventana, text="", width=ww, height=hh)
    btn33 = tk.Button(ventana, text="", width=ww, height=hh)

    px = py = 2
    btn11.grid(row=1, column=1, padx=px, pady=py)
    btn12.grid(row=1, column=2, padx=px, pady=py)
    btn13.grid(row=1, column=3, padx=px, pady=py)
    btn21.grid(row=2, column=1, padx=px, pady=py)
    btn22.grid(row=2, column=2, padx=px, pady=py)
    btn23.grid(row=2, column=3, padx=px, pady=py)
    btn31.grid(row=3, column=1, padx=px, pady=py)
    btn32.grid(row=3, column=2, padx=px, pady=py)
    btn33.grid(row=3, column=3, padx=px, pady=py)

    btnPlay = tk.Button()

    btnAnalytics = tk.Button()

    btnExit = tk.Button(ventana, text="Exit", width=10, height=2, command=exit)
    btnExit.grid(row=4, column=1, columnspan=1, padx=5, pady=25)

    ventana.mainloop()


if __name__ == '__main__':
    show_window()
