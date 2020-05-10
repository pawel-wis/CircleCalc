import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        self.master = master
        master.title('Kalkulator pola')


        self.label = tk.Label(master, text='Podaj promien')
        self.label.grid(row=0, column=0)

        self.input = tk.Entry(master)
        self.input.grid(row=0, column= 0)

        self.btn = tk.Button(master, text='Oblicz')
        self.btn.grid(row=1, columnspan=2)

        self.res_label = tk.Label(master, text='')
        self.res_label.grid(row=2, columnspan=2)



root = tk.Tk()
app = App(root)
root.mainloop()
