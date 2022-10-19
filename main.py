from pessoa import Pessoa

nome = input("Digite o nome da pessoa :")
datanasc = float(input("Digite ano de nascimento :"))
altura = float(input("Digite a altura :"))

pessoa = Pessoa(nome, datanasc, altura)

print("O nome da pessoa é", pessoa.get_nome())
print("A idade  é", pessoa.idade1())
print("A altura da pessoa é: ", pessoa.get_altura())