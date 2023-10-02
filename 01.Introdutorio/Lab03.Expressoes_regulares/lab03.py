# https://docs.python.org/3/library/re.html

import re

texto = "Meu email é exemplo@gmail.com e você pode me contatar em outro_email@hotmail.com"
print(texto)

# Expressão regular para contar quantas vezes o caracter '@' aparece no texto
resultado = len(re.findall("@", texto))

print(f"O caractere '@' apareceu {resultado} vezes no texto.")

# Expressão regular para extrair a palavra que aparece após a palavra "você" em um texto
resultado = re.findall(r"você (\w+)", texto)

print(f"A palavra após 'você' é: {resultado[0]}.")


# NOTA: O r antes da string que representa a expressão regular em Python é usado para indicar que a string é uma literal raw. Isso significa que as barras invertidas (\) não são
# interpretadas como caracteres de escape, mas são incluídas na expressão regular como parte do padrão.

# Expressão regular para extrair endereços de e-mail de uma string
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", texto)
print(emails)

text = "O aluno estava incrivelmente perdido, mas encontrou a DSA e rapidamente começou a aprender."

# Extraindo os advérbios da frase
for m in re.finditer(r"\w+mente\b", text):
    print("%02d-%02d: %s" % (m.start(), m.end(), m.group(0)))