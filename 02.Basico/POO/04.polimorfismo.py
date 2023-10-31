class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print("O carro está acelerando.")

    def frear(self):
        print("O carro está freando.")

class Moto(Veiculo):
    def acelerar(self):
        print("A moto está acelerando.")

    def frear(self):
        print("A moto está freando.")

class Aviao(Veiculo):
    def acelerar(self):
        print("O avião está acelerando.")

    def frear(self):
        print("O avião está freando.")

    def decolar(self):
        print("O avião está decolando.")



lista_veiculos = [Carro("Porsche", "911 Turbo"), Moto("Honda", "CB 1000R Black Edition"), Aviao("Boeing", "757")]

print(type(lista_veiculos))

for item in lista_veiculos:
    item.acelerar()
    item.frear()

    if isinstance(item, Aviao):
        item.decolar()

    print("---")