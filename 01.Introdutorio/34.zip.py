# A função zip() agrupa elementos de múltiplas estruturas de dados iteráveis juntos em pares, ela retorna um objeto zip, que pode ser convertido em
# outra estrutura de dados, como uma lista ou dicionário, se necessário

x = [1,2,3]
y = [4,5,6]

# Unindo as listas, em Python3 retorna um iterator
zip(x,y)

# zip retorna tuplas. Neste caso, uma lista de tuplas
print(list(zip(x,y)))

# Atento quando as sequências possuirem número diferente de elementos
print(list(zip("ABCD", "xy"))) # Se ela não conseguir combinar, descartará os elementos, output: [('A', 'x'), ('B', 'y')]

a = [1,2,3]
b = [4,5,6,7,8]

print(list(zip(a,b)))

d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

# zip vai unir as chaves, porque sao os primeiros elementos
print(list(zip(d1,d2)))

# unindos os valores (items)
print(list(zip(d1,d2.values())))

# Criando uma função para trocar valores entre 2 dicionários
def trocaValores(d1, d2):

    dicTemp = {}

    for d1key, d2val in zip(d1,d2.values()):
        dicTemp[d1key] = d2val

    return dicTemp

print(trocaValores(d1,d2))