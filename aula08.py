# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'Luiz', 'idade': 24}
p1 = Pessoa(**dados)
p1.__dict__['outra'] = 'coisa'

print(vars(p1))
