# Tudo em Python é um objeto. E cada objeto tem métodos e atributos.

# Atributos são propriedades, características do objeto.
# Métodos são funções com ações que podem ser executadas nos objetos.

lista = [100,-2,12,65,0]
print(type(lista))

print(lista)

lista.append(100)

print(lista)

print(lista.count(100))

# A função help() explica como utilizar algum método de um objeto
#help(lista.count)

# A função dir() mostra todos os métodos e atributos de um objeto
#print(dir(lista))

frase = "Isso é uma string"
print(type(frase))

#print(dir(frase))

print(frase.split())