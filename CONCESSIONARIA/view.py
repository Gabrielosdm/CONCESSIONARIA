from tkinter import *
from view2 import Carros

class Login(Tk):
    def __init__(self):
        super().__init__()


        self['bg'] = 'gray14'
        self.geometry('400x400+750+100')
        self.title('Login')
        self.font = ('Verdana', '14', 'bold')


        self.lb = Label(self ,text = 'BEM VINDO!',font = self.font)
        self.lb.place(x=130,y=30)
        self.lb2 = Label(self , text = 'Nome do vendedor :',bg = 'gray14',fg = 'white')
        self.lb2.place(x=10, y=100)
        self.lb3 = Label(self, text='Nome do Cliente :',bg = 'gray14',fg = 'white')
        self.lb3.place(x=10, y=130)
        self.lb4 = Label(self ,text = 'Data da compra :',bg = 'gray14',fg = 'white')
        self.lb4.place(x=10 ,y=200)
#entrys
        vendedor = Entry(self)
        vendedor.place(x=128, y=100)
        cliente = Entry(self)
        cliente.place(x=115, y=130)
        data = Entry(self)
        data.place(x=109, y=200)
#botao confirm
        self.bt = Button(self ,width=10, height=3,bg='lime green', text='Confirmar',command = self.criar_janela)
        self.bt.place(x=300,y=320)


    def criar_janela(self):
        Carros(self)

