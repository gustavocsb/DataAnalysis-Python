# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.



class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

    def print_smartphone(self):
        print(f'Tamanho: {self.tamanho}\nInterface: {self.interface}\n')

class MP3Player(Smartphone):
    def __init__(self, capacidade, tamanho, interface):
        super().__init__(tamanho, interface)
        self.capacidade = capacidade

    def print_smartphone(self):
        print(f'Capacidade: {self.capacidade}')
        super().print_smartphone()

sm01 = Smartphone('Pequeno', 'Touchscreen')

sm01.print_smartphone()

mp01 = MP3Player('64GB', 'Pequeno', 'Touchscreen')

mp01.print_smartphone()
