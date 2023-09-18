# Para declarar uma lista, começa e fecha com [ ]
lista_1 = ["arroz, frango, tomate, leite"]
print(type(lista_1))
print(lista_1)

lista_2 = ["arroz", "frango", "tomate", "leite"]
print(type(lista_2))
print(lista_2)

lista_3 = [23, 100, "Cientista de Dados"]
print(type(lista_3))
print(lista_3)

item1 = lista_3[0]
item2 = lista_3[1]
item3 = lista_3[2]

print(item1, item2, item3)

# Atualizando um item da lista
print(lista_2[2])
lista_2[2] = "chocolate"
print(lista_2)

# Deletando um item da lista
# Não é possível deletar um item que não existe na lista, gerará erro
#del(lista_2[4])
del(lista_2[3])

print(lista_2)

# Lista de Listas (Listas Aninhadas)
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
print(listas)

a = listas[0]
print(a)

b = a[0]
print(b)

list1 = listas[1]
print(list1)

valor_1_0 = list1[0]
print(valor_1_0)

valor_1_2 = list1[2]
print(valor_1_2)

list2 = listas[2]
print(list2)

valor_2_0 = list2[0]
print(valor_2_0)

# Operações com listas
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

a = listas[0][0]
print(a)
b = listas[1][2]
print(b)
c = listas[0][2] + 10
print(c)
d = 10
print(d)
e = d * listas[2][0]
print(e)

# Concatenando listas
lista_s1 = [34, 32, 56]
print(lista_s1)
lista_s2 = [21, 90, 51]
print(lista_s2)

lista_concatenada = lista_s1 + lista_s2
print(lista_concatenada)

# Operador in
lista_teste_op = [100, 2, -5, 3.4]
print(10 in lista_teste_op)
print(100 in lista_teste_op)

# Funções Built-in
lista_numeros = [10, 20, 50, -3.4]

# Função len() retorna o comprimento da lista
print(len(lista_numeros))

# Função max() retorna o valor máximo da lista
print(max(lista_numeros))

# Função min() retorna o valor mínimo da lista
print(min(lista_numeros))

lista_formacoes = ["Analista de Dados", "Cientista de Dados", "Engenheiro de Dados"]
print(lista_formacoes)

# Adicionando um item a lista
lista_formacoes.append("Engenheiro de IA")
print(lista_formacoes)

lista_formacoes.append("Engenheiro de IA")
print(lista_formacoes)
lista_formacoes.append("Engenheiro de IA")
print(lista_formacoes)

a = []
print(a)
print(type(a))
a.append(10)
print(a)
a.append(50)
print(a)

old_list = [1,2,5,10]
new_list = []
print(old_list)

for item in old_list:
    new_list.append(item)
    print(new_list)

cidades = ["Recife", "Manaus", "Salvador"]
cidades.extend(["Fortaleza", "Palmas"])
print(cidades)

print(cidades.index("Salvador"))
# "Rio de Janeiro" não está na lista, gerará erro
#print(cidades.index("Rio de Janeiro"))

# No índice [2], inserir o número 110
cidades.insert(2,110)
print(cidades)

cidades.remove(110)
print(cidades)

cidades.reverse()
print(cidades)

x = [3,4,2,1]
x.sort()
print(x)

