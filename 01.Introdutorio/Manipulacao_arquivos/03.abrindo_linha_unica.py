# Abrindo dataset em linha única
f = open(r"01.Introdutorio\Manipulacao_arquivos\arquivos\salarios.csv", "r")

data = f.read()
rows = data.split("\n")

print(rows)

