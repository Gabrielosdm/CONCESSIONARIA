from tkinter import *
from view3 import Detalhes

class Carros(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.font = ('Verdana', '14', 'bold')
        self.font2 = ('Verdana','10','bold')

        self['bg'] = 'gray14'
        self.geometry('400x400+750+100')
        self.title('Concessionária - CARROS')
        self.transient(parent)
        self.grab_set()

        self.bt1 = Button(self, width=11, height=5, text="Bmw X5", bg = 'gold',font = self.font2, command=Detalhes)
        self.bt2 = Button(self, width=11, height=5, text="New Civic", bg = 'gold',font = self.font2, command=Detalhes)
        self.bt3 = Button(self, width=11, height=5, text="Audi A7", bg='gold',font = self.font2, command=Detalhes)
        self.bt4 = Button(self, width=11, height=5, text="Camaro", bg='gold',font = self.font2, command=Detalhes)
        self.bt5 = Button(self, width=11, height=5, text="Corvette", bg='gold',font = self.font2, command=Detalhes)

        self.lb = Label(self ,text='CONCESSIONÁRIA', font = self.font)
        self.lb.place(x=100, y=5)
        self.lb2 = Label(self, text='ESCOLHA O CARRO', font = self.font2)
        self.lb2.place(x=25,y=70)

        self.bt1.place(x=25, y=100)
        self.bt2.place(x=145, y=100)
        self.bt3.place(x=265, y=100)
        self.bt4.place(x=25, y=230)
        self.bt5.place(x=145, y=230)