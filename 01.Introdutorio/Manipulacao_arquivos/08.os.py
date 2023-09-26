import os

texto = "Cientista de Dados pode ser uma excelente alternativa de carreira.\n"
texto += "Esses profissionais precisam saber como programar em Python.\n"
texto += "E, claro, devem ser proficientes em Data Science."

print(texto)

# Criando um arquivo
arquivo = open(os.path.join('01.Introdutorio/Manipulacao_arquivos/arquivos/cientista.txt'), "w")

# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + ' ')

# Fechando o arquivo
arquivo.close()

# Lendo o arquivo
arquivo = open(r"01.Introdutorio\Manipulacao_arquivos\arquivos\cientista.txt", "r")
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

# ------------------------------ Expressão with ------------------------------
with open (r"01.Introdutorio\Manipulacao_arquivos\arquivos\cientista.txt", "r") as arquivo:
    conteudo = arquivo.read()

# o método close() é executado automaticamente

print(len(conteudo))
print(conteudo)

with open(r"01.Introdutorio\Manipulacao_arquivos\arquivos\cientista.txt", "w") as arquivo:
    arquivo.write(texto[:19])
    arquivo.write("\n")
    arquivo.write(texto[28:66])

# Lendo o arquivo
arquivo = open(r"01.Introdutorio\Manipulacao_arquivos\arquivos\cientista.txt", "r")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

