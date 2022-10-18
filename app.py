from figura_geometrica import FiguraGeometrica
triangulo = FiguraGeometrica(3, 4, "triangulo")
quadrado = FiguraGeometrica(3, 3, "quadrado")
retangulo = FiguraGeometrica(10, 5, "")

print("O valor da área do triangulo é: ", triangulo.calcular_area())
print("O valor da área do quadrado é: ", quadrado.calcular_area())
print("O valor da área do retangulo é: ", retangulo.calcular_area())

print("O valor da altura antes da mudamça: ", triangulo.get_altura())
#triangulo.set_lado(2)
#triangulo.set_altura(5)
#print("O valor da altura após a mudança: ", triangulo.get_altura())
#area = (triangulo.get_altura(3) * triangulo.get_lado(3)) / 2
#print("O valor da area é: ", area)