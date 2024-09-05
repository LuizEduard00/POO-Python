# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023 # att de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')  


p1 = Pessoa('Luiz', 24)
print(Pessoa.ano)

Pessoa.metodo_de_classe()