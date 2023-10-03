import re

# Variável do tipo String
lyrics = '''
Todos os dias quando acordo
Não tenho mais
O tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço
Como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo
Que esse sangue amargo
E tão sério
E selvagem! Selvagem!
Selvagem!
Veja o sol
Dessa manhã tão cinza
A tempestade que chega
É da cor dos teus olhos
Castanhos
Então me abraça forte
E diz mais uma vez
Que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens! Tão jovens!
'''

print(lyrics)

# 1. Criar um REGEX para contar quantas vezes o caractere 'a' aparece na lyrics.
# 2. Contar quantas vezes a palavra 'tempo' aparece na música.
# 3. Extrair as palavras seguidas por exclamação.
# 4. Extrair quaisquer palavras cujo antecessor seja 'esse' e o sucessor seja a palavra 'amargo'.
# 5. Retornar as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento.

# ****************************************************************************************************************************************************************************
# 1.
#contador = re.findall("a", lyrics)
#resultado = len(contador)

# Contando apenas 'a'
#resultado = len(re.findall("a", lyrics))

# Contando 'a' e 'A'
resultado = len(re.findall("a", lyrics, re.IGNORECASE))

print(f"O caractere 'a' aparece {resultado} vezes na lyrics.")

# ****************************************************************************************************************************************************************************
# 2.
resultado = len(re.findall(r"\btempo\b", lyrics))

print(f"A palavra 'tempo' apareceu {resultado} vezes na lyrics.")

# ****************************************************************************************************************************************************************************
# 3.
resultado = re.findall(r"\b\w+!", lyrics)

print(f"As palavras seguidas por exclamação são: {resultado}")

# ****************************************************************************************************************************************************************************
# 4.
resultado = re.findall(r"\besse\s(\w+)\samargo\b", lyrics)

print(f"As palavras entre 'esse' e 'amargo' são: {resultado}")

# ****************************************************************************************************************************************************************************
# 5.
resultado = re.findall(r"\b[\wÀ-ÿ]+[áéíóúãõç]", lyrics)

print(f"As palavras acentuadas são: {resultado}")