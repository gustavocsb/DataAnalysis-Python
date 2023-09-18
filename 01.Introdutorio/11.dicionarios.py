# É uma lista:
estudantes_lista = ["Pedro", 24, "Ana", 22, "Ronaldo", 26, "Janaina", 25]
print(estudantes_lista)
print(type(estudantes_lista))

# É um dicionário:
estudantes_dict = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}
print(estudantes_dict)
print(type(estudantes_dict))

print(estudantes_dict["Pedro"])

# Adicionando a chave "Marcelo" com valor 23
estudantes_dict["Marcelo"] = 23
print(estudantes_dict["Marcelo"])

# Limpando o dicionário
estudantes_dict.clear()
print(estudantes_dict)

del estudantes_dict
# Gerará erro, visto que foi deletado anteriormente
#print(estudantes_dict)

estudantes = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}
# O tamanho é 4 pois cada elemento é contado como um par, chave:valor
print(len(estudantes))

print(estudantes.keys()) # Retornará apenas as chaves, neste caso os nomes
print(estudantes.values()) # Retornará apenas os valores, neste caso os números após os nomes
print(estudantes.items()) # Retornará as chaves e valores

estudantes2 = {"Camila":27, "Adriana":28, "Roberta":26}
print(estudantes2)

estudantes.update(estudantes2)
print(estudantes)

dic1 = {}
print(dic1)
# A chave é uma string eo valor um int
dic1["chave_um"] = 2
print(dic1)
# A chave é um float e o valor uma string, ainda sendo aceito pela linguagem
dic1[9.13] = "Python"
print(dic1)
# A chave é um int e o valor é um int
dic1[10] = 5
print(dic1)
dic1["teste"] = 5
print(dic1)

dict1 = {}
print(dict1)
dict1["teste"] = 10
dict1["key"] = "teste"
print(dict1)

dict2 = {}
dict2["key1"] = "Data Science"
dict2["key2"] = 10
dict2["key3"] = 100
print(dict2)

a = dict2["key1"]
b = dict2["key2"]
c = dict2["key3"]

print(a,b,c)

# Dicionário de listas
dict3 = {"chave":1230, "chave2":[22,453,73.4], "chave3":["picanha", "fraldinha", "alcatra"]}
print(dict3)
print(dict3["chave2"])
print(dict3["chave3"][0].upper())

var1 = dict3["chave2"][0] - 2
print(var1)

dict3["chave2"][0] -= 2
print(dict3)

# Criando dicionários aninhados
dict_aninhado = {"key1":{"key2_aninhada":{"key3_aninhada":"Dict aninhado em Python"}}}
print(dict_aninhado)
print(dict_aninhado["key1"]["key2_aninhada"]["key3_aninhada"])
