# Super-classe Animal
class Animal():
    def __init__(self):
        print("Animal criado")

    def imprimir(self):
        print("Este é um animal")

    def comer(self):
        print("Hora de comer")

    def emitir_som(self):
        pass

# Classe cachorro - Sub-classe de Animal
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto cachorro criado")

    def emitir_som(self):
        print("Woof Woof")

# Classe gato - Sub-classe de Animal
class Gato(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado")

    def emitir_som(self):
        print("Meow meow")

rex = Cachorro()
zeze = Gato()

rex.imprimir()
rex.comer()

zeze.imprimir()
zeze.comer()