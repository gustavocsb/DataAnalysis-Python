# Condicional if
if 5 > 2:
    print("A sentença é verdadeira.")

# Condicional if... else
if 5 < 2:
    print("A sentença é verdadeira.")
else:
    print("A sentença é falsa.")

# Condicional if... else com variável
dia = "Terça"
if dia == "Segunda":
    print("Hoje fará sol.")
else:
    print("Hoje vai chover.")

if dia == "Segunda":
    print("Hoje fará sol.")
elif dia == "Terça":
    print("Hoje vai chover.")
else:
    print("Sem previsão do tempo para o dia selecionado.")