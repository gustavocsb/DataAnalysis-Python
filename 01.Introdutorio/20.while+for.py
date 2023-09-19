import time

tempo_inicio = time.time()
# Encontrando números primos entre 2 e 30 usando loop for e while

# Variável para armazenar números primos
primos = []

# Loop for para percorrer números de 2 a 30
for num in range(2,31):
    # Variável de controle
    primo = True
    # Loop while para verificar se o número é primo
    i = 2
    while i <= num // 2:
        if num % i == 0:
            primo = False
            break
        i+=1
    # Adicionando o número primo na lista
    if primo:
        primos.append(num)
# Imprimindo a lista de números primos
print(primos)

tempo_final = time.time()

tempo_execucao = tempo_final - tempo_inicio
#print(f"Tempo de execução: "+time.strftime("%H:%M:%S", time.gmtime(tempo_execucao)))
print("Tempo de execução:",tempo_execucao,"segundos")

tempo_inicio = 0
tempo_inicio = time.time()

for i in range(2,31):
    j = 2
    valor = 0
    while j < i:
        if i % j == 0:
            valor = 1
            j+=1
        else:
            j+=1
    if valor == 0:
        print(i,"é um número primo")
        valor = 0
    else:
        valor = 0

tempo_final = 0
tempo_final = time.time()

tempo_execucao = 0
tempo_execucao = tempo_final - tempo_inicio
print("Tempo de execução:",tempo_execucao,"segundos")