# Abrindo o arquivo para leitura: open(r"diretório")
arq1 = open(r"01.Introdutorio\Manipulacao_arquivos\arquivos\arquivo1.txt")

print(type(arq1))

# Lendo o arquivo e printando seu conteúdo
print(arq1.read())

# Contar o número de caracteres
print(arq1.tell())

# Após ler o arquivo, precisa retornar para o início do arquivo
print(arq1.seek(0,0))

# Lendo apenas os primeiros 23 caracteres
print(arq1.read(23))

# Lendo sem retornar para o início do arquivo
print(arq1.read())