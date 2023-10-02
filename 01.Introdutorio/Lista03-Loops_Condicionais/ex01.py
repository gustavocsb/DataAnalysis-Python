# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"


# Método pedido pelo exercício
diaCorreto = False
while diaCorreto == False:
    dia=input("Informe o dia de hoje: ")
    if dia.lower() not in ["sabado", "domingo", "segunda", "terça", "quarta", "quinta", "sexta"]:
        print("Dia incorreto! Digite corretamente:\nSegunda\t\tTerça\t\tQuarta\t\tQuinta\t\tSexta\t\tSabado\t\tDomingo")
    else:
        diaCorreto = True
        if dia.lower() in ["sabado", "domingo"]:
            print("Hoje é dia de descanso!")
        else:
            print("Você precisa trabalhar hoje!")



import datetime
# Método sem input, extraindo o dia atual usando datetime

dias = {0:"segunda", 1:"terça", 2:"quarta", 3:"quinta", 4:"sexta", 5:"sabado", 6:"domingo"}
today = datetime.datetime.today().weekday()

if dias[today] in ["sabado", "domingo"]:
    print("Hoje é dia de descanso!")
else:
    print("Você precisa trabalhar hoje!")
