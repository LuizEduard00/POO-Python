# Métodos em instâncias de classes Python
# Hard Coded - É algo que foi escrito diretamete no código
#Método é uma função dentro de uma classe
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando.')

fusca = Carro('Fusca')
print(fusca.nome)

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()