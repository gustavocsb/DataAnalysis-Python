# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def listaAppend (lista):
    if len(lista) == 4:
        lista.append(15)
        lista.append(25)
    else:
        print("A lista inserida não possui 4 elementos")
    return (lista)

#lista = listaAppend([15,20,31])
lista = listaAppend([12,971,12,25])

print(lista)
