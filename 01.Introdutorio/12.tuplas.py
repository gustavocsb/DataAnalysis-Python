# Tuplas foram feitas para serem imutáveis
tupla1 = ("Geografia", 23, "Elefantes", 9.8, "Python")
print(tupla1)

# Tuplas não suportam append()
#tupla1.append("Chocolate")

# Tuplas não suportam delete de um item específico
#del tupla1["Elefantes"]

tupla1 = ("Chocolate")
print(tupla1)

tupla1 = ("Geografia", 23, "Elefantes", 9.8, "Python")
print(tupla1[0])

print(len(tupla1))

print(tupla1[1:])

print(tupla1.index("Elefantes"))

# Tuplas não suportam atribuição de item
#tupla1[1] = 21

# Deletando a tupla
del tupla1
# Não printará, visto que foi deletado
#print(tupla1)

t2 = ('A', 'B', 'C')
print(t2)

# Convertendo uma tufa para uma lista:
lista_t2 = list(t2)
print(type(t2))
print(type(lista_t2))
print(lista_t2)

lista_t2.append('D')

# Convertendo a lista para tufa
t2 = tuple(lista_t2)
print(t2)