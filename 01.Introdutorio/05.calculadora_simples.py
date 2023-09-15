print("--- Calculadora simples ---")

num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))

operacao = int(input("\nSoma - 1\nSubtração - 2\nMultiplicação - 3\nDivisão - 4\n\nDigite um número de 1 a 4 com a operação desejada: "))

if operacao == 1:
    soma = num1 + num2
    #print("A soma de "+str(num1)+" + "+str(num2)+" é: "+str(soma))
    print(f"A soma de {num1} + {num2} é: {soma}")
elif operacao == 2:
    subtracao = num1 - num2
    print(f"A subtração de {num1} - {num2} é: {subtracao}")
elif operacao == 3:
    multiplicacao = num1 * num2
    print(f"A multiplicação de {num1} * {num2} é: {multiplicacao}")
elif operacao == 4:
    divisao = num1 / num2
    print(f"A divisão de {num1} / {num2} é: {divisao}")
else:
    print("Número inválido!")


    