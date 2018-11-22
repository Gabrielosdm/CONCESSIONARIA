from tkinter import *

class Detalhes(Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry("400x400+750+100")
        self.title("Detalhes compra")
        self["bg"] = 'gray14'
        self.font = ('Verdana', '14', 'bold')

        self.lb = Label(self ,text='Compra efetuada',bg = 'gray14',fg = 'white',font = self.font)
        self.lb.place(x=20,y=30)