print('Strings em Python')
print("Se pode usar aspas duplas ou simples para strings em Python")

# Indexando Strings
s = "Gustavo Caldas Silveira Borges"
print(s)

print(s[0])
print(s[1])
print(s[2])
print(s[3])

# ----- Pode-se usar um : para executar um slicing que faz a leitura de tudo até um ponto designado -----
# Retorna todos os elementos da string, começando pela posição definida
print(s[1:])

# Retorna todos os elementos da string, finalizando pela posição definida
print(s[:3])

# Indexação negativa, para ler de trás para frente
print(s[-1])

# Retorna tudo, exceto o último elemento
print(s[:-1])

# Slicing também pode ser usado em pedaços específicos
# Exemplos:
print(s[::1])

# Retornando a string a cada 2 elementos
print(s[::2])

# Retornando a string ao contrário
print(s[::-1])

print(f"{s} é um ótimo profissional de Data Science")
print(s)

s = s + " é um ótimo profissional de Data Science"
print(s)

letra = "w"
print(letra*3)

# ----- Funções Built-in de Strings -----
# Upper Case
print(s.upper())

# Lower Case
print(s.lower())

# Dividir uma string por espaços (em branco por padrão)
print(s.split())

# Dividir uma string por um elemento específico
print(s.split("a"))

s = "estudar Python é emocionante!"

print(s.capitalize())

print(s.count("e"))

print(s.isalnum())

print(s.islower())

print(s.isspace())

print(s.endswith("o"))

# Comparando Strings

print("Python" == "R")
print("Python" == "Python")
