class View:
    def __init__(self):
        self.control = None
    #guarda control associada
    def set_control(self,control):
        self.control = control
    def exibir_menu(self):
        resposta=True
        while resposta:
            print('''
            1.Exibir lista
            2.Incluir item
            3.Excluir item
            4.Sair
            ''')
            resposta = input('Digite um número: ')
            if resposta == '1':
                print('\n Lista de itens')
                self.exibir_lista_compras(self.control.get_lista_compras())
            elif resposta == '2':
                print('\n Item incluído')
            elif resposta == '3':
                print('\n Item excluído')
            elif resposta == '4':
                print('\n Tchau!')
                resposta=False
            else:
                print('\n Valor incorreto')
    #exibir lista de compras
    def exibir_lista_compras(self,lista_compras):
        for chave,valor in lista_compras.items:
            print(f'-{chave}:{valor}')