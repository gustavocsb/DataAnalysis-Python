# Abrindo arquivo para gravação
# Senão houver arquivo2, ele criará, se já houver, ele irá sobrescrever
arq2 = open(r"01.Introdutorio\Manipulacao_arquivos\arquivos\arquivo2.txt", "w")

# Como abrimos o arquivo apenas para gravação, não podemos usar comandos de leitura
#print(arq2.read())

# Gravando arquivo
arq2.write("Voltando a programar em Python!")
# Fechando o arquivo, após aberto
arq2.close()

arq2 = open(r"01.Introdutorio\Manipulacao_arquivos\arquivos\arquivo2.txt", "a") # a = append
arq2.write(" E a metodologia de ensino da DSA facilita esse retorno.")
arq2.close()