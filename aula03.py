# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Luiz', 'Eduardo')
# p1.nome = "Luiz"
# p1.sobrenome = "Eduardo"

p2 = Pessoa('Rafael', 'Oliveira')
# p2.nome = "Rafael"
# p2.sobrenome = "Oliveira"


print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)
