# conceito de classes

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def imprimir_nome(self):
        print(f'nome: {self.nome} idade: {self.idade} ano(s)')



p = Pessoa('victor', 20)


p.imprimir_nome()

