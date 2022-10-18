from codecs import latin_1_decode


class FiguraGeometrica:
    def __init__(self, lado, altura, nome):
        self.__lado = lado
        self.__altura = altura
        self.__nome = nome

    def get_lado(self):
        return self.__lado
    def set_lado(self, lado):
        self.__lado = lado
    def get_altura(self):
        return self.__altura
    def set_altura(self, altura):
        self.__altura = altura
    def get_nome(self):
        return self.__nome 
    def set_nome(self, nome):
        self.__nome = nome

    def calcular_area(self):
        area = self.get_altura() * self.get_lado() / 2
        return area

