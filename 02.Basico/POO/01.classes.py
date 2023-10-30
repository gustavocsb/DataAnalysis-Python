class Livro():
    # Método construtor, seu nome é __init__
    # o parâmetro self é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)
    def __init__(self):
        self.titulo = 'Sapiens - Uma Breve História da Humanidade'
        self.isbn = 9988888
        print("Construtor chamado para criar um objeto desta classe")

    def imprimir(self):
        print(f"Foi criado o livro {self.titulo} com ISBN {self.isbn}")

Livro1 = Livro()

print(type(Livro1))

print(Livro1.titulo)

Livro1.imprimir()

class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe")

    def imprimir(self):
        print(f"Foi criado o livro {self.titulo} com ISBN {self.isbn}")
        
Livro2 = Livro("O Poder do Hábito", 77886611)

print(Livro2.titulo)

Livro2.imprimir()

class Algoritmo():
    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamado para criar um objeto desta classe")

algo1 = Algoritmo(tipo_algo = "Random Forest")

algo2 = Algoritmo(tipo_algo = "Deep Learning")

print(algo1.tipo)

print(algo2.tipo)

lst_num = ["Data", "Science", "Academy", "Nota", 10, 10]

print(type(lst_num))

print(type([]))
        
print(lst_num.count(10))         

print(type(10))
print(type([]))
print(type(()))
print(type({}))
print(type("a"))

class Carro(object):
    pass

ferrari = Carro()

print(type(ferrari))

class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

Estudante1 = Estudantes("Bob", 12, 9.5)

print(Estudante1.nome)
print(Estudante1.idade)
print(Estudante1.nota)

class Funcionarios:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        print("Construtor chamado para criar um objeto desta classe")

    def listFunc(self):
        print(f"Funcionário(a) {self.nome} tem salário de R$ {str(self.salario)} e o cargo é {self.cargo}")

Func1 = Funcionarios("Mary", 20000, "Cientista de Dados")

Func1.listFunc()

print("***** Usando atributos *****")

# Has attribute, True ou False se tiver este atributo no objeto ou não
print(hasattr(Func1, "nome"))
print(hasattr(Func1, "salario"))

# Set attribute, dando um update no atributo do objeto
print(Func1.salario)
setattr(Func1, "salario", 4500)
print(Func1.salario)
print(hasattr(Func1, "salario"))

# Get attribute, retornando o valor do atributo, método padrão GET
print(getattr(Func1, "salario"))

# Delete attribute, deletando um atributo do objeto
delattr(Func1, "salario")
print(hasattr(Func1, "salario")) # checando se o atributo foi deletado
