# Dividindo um arquivo em colunas
f = open(r"01.Introdutorio\Manipulacao_arquivos\arquivos\salarios.csv", "r")
data = f.read()
rows = data.split("\n")
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

print(full_data)