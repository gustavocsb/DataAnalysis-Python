# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa:
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def print_pessoa(self):
        print(f'Nome: {self.nome}\nCidade: {self.cidade}\nTelefone: {self.telefone}\nEmail: {self.email}\n')

    def add_telefone(self, telefone):
        self.telefone.append(telefone)

pe01 = Pessoa('Gustavo', 'Brasília', ['(61) 99999-9999'], 'gustavo@outlook.com')        

pe01.print_pessoa()

pe01.add_telefone('(61) 98888-8888')

pe01.print_pessoa()