import math

def numPrimo(num):
    if (num%2) == 0 and num>2:
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return ("Este número não é primo")
    return "Este número é primo"

print(numPrimo(541))
print(numPrimo(2))

caixa_baixa = "Este Texto Deveria Estar Todo em LowerCase"

def lowercase(text):
    return text.lower()

lowercased_string = lowercase(caixa_baixa)

print(lowercased_string) 

# Fazendo split dos dados
def split_string_palavras(text):
    return text.split(" ")

texto = "Esta função será bastante útil para separar grandes volumes de dados"

# Isso divide a string em uma lista de palavras
print(split_string_palavras(texto))

# Podemos atribuir o output de uma função para uma variável
token = split_string_palavras(texto)

print(token)

# Fazendo split dos dados

def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)

split_string_letras(texto)