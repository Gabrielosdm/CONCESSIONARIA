class Model:
    def __init__(self):
        self.lista_compras = open('estoque','r')

    def get_lista_compras(self):
        return self.lista_compras
