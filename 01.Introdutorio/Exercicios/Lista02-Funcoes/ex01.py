# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números

def pares_1a20():
    lista=range(1,21)
    for i in lista:
        if i % 2 == 0:
            print(i)

def pares_1a20v2():
    for i in range(2,21,2):
        print(i)

pares_1a20()

pares_1a20v2()