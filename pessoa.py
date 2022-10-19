class Pessoa:
    def __init__(self, nome, datanasc, altura):
        self.__nome = nome
        self.__datanasc = datanasc
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_datanasc(self):
        return self.__datanasc

    def set_datanasc(self, datanasc):
        self.__datanasc = datanasc
    
    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def idade_atual(self):
        nova_idade = 2022
        return nova_idade

    def idade1(self):
        idade_nova = self.idade_atual() - self.get_datanasc()
        return idade_nova

        