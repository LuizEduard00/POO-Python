#a Atributos de classe

class Pessoa:
    atributo ='valor'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        ...
p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)