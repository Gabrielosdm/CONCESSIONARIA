class Control:
    def __init__(self,view,model):
        self.view = view
        self.model=model

    def exibir_menu(self):
        self.view.exibir_menu()
    def get_lista_compras(self):
        return self.model.get_lista_compras()


