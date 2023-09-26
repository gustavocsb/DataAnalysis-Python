# Contando o número de colunas de um arquivo
f = open (r"01.Introdutorio\Manipulacao_arquivos\arquivos\salarios.csv", "r")

data = f.read()
rows = data.split("\n")
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]

count = 0

for column in first_row:
    count+=1

# Outra solução
#for column in full_data[0]:
#   count+=1

print(count)