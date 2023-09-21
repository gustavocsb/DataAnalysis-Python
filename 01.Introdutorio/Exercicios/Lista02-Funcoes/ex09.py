# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]

palavras_m = [x for x in palavras if "a" in x]

print(palavras_m)