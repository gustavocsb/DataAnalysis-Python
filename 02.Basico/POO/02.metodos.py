class Circulo():
    pi = 3.14
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return (self.raio * self.raio) * Circulo.pi
    
    def setRaio(self, raio):
        self.raio = raio

    def getRaio(self):
        return self.raio
    
circ = Circulo(12)

print(circ.getRaio())
print(circ.area())

circ1 = Circulo(7)

print(f"O raio é: {circ1.getRaio()}")
print(f"A área é igual a: {circ1.area()}")

circ1.setRaio(3)
print(f"Novo raio igual a: {circ1.getRaio()}")