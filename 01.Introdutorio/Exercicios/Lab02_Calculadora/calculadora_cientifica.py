# Calculadora científica em Python
import math

def soma(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

def quadrado(num):
    return num**2

def potencia(n1,n2):
    return n1**n2

def raiz(num):
    return math.sqrt(num)

def exponencial(num):
    return math.exp(num)

def logaritmo(n1,n2):
    return math.log(n1,n2)

def seno(num):
    return math.sin(num)

def cosseno(num):
    return math.cos(num)

def tangente(num):
    return math.tan(num)

def seno_inverso(num):
    return math.asin(num)

def cosseno_inverso(num):
    return math.acos(num)

def tangente_inverso(num):
    return math.atan(num)

def fatorial(num):
    return math.factorial(num)

def digitar_n1_n2():
    n1=float(input("Digite o primeiro número: "))
    n2=float(input("Digite o segundo número: "))
    return n1,n2

def digitar_num():
    num=float(input("Digite o número: "))
    return num

def digitar_num_1():
    while True:
        num=float(input("Digite um número entre -1 e 1: "))
        if -1 <= num <= 1:
            return num
        else:
            print("Número inválido. Tente novamente!")

def pause():
    input("Pressione ENTER para continuar...")
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    

saida=0
operacoes = {1:soma, 2:subtracao, 3:multiplicacao, 4:divisao, 5:quadrado, 6:potencia, 7:raiz, 8:exponencial, 9:logaritmo, 10:seno, 11:cosseno, 12:tangente, 
             13:seno_inverso, 14:cosseno_inverso, 15:tangente_inverso, 16:fatorial}

while saida == 0:
    print("------- Calculadora Científica -------")
    print("Funções:")
    print("1. Soma (+)          2. Subtração (-)")
    print("3. Mult. (*)         4. Divisão (÷)")
    print("5. Quadrado (²)      6. Potência (xⁿ)")
    print("7. Raiz quad. (√)    8. Exponencial (Eˣ)")
    print("9. Log. (log₁₀x)     10. Seno(x)")
    print("11. Cosseno(x)       12. Tangente(x)")
    print("13. Seno⁻¹(x)        14. Cosseno⁻¹(x) ")
    print("15. Tangente⁻¹(x)    16. Fatorial (!)")
    print("0 - Sair")
    aux = int(input("Escolha uma operação: "))
    if aux == 0:
        while True:
            confirmaSaida=input("Tem certeza que deseja sair? (S/N)\n")
            if confirmaSaida.lower() in ["s","n"]:
                break
            else:
                print("Letra inválida, responda com 'S' ou 'N' ")
        if confirmaSaida.lower() == "s":
            saida = 1
    elif aux in operacoes:
        if aux == 1:
            n1,n2=digitar_n1_n2()
            print(f"{n1} + {n2} =",soma(n1,n2))
            pause()
        elif aux == 2:
            n1,n2=digitar_n1_n2()
            print(f"{n1} - {n2} =",subtracao(n1,n2))
            pause()
        elif aux == 3:
            n1,n2=digitar_n1_n2()
            print(f"{n1} * {n2} =",multiplicacao(n1,n2))
            pause()
        elif aux == 4:
            n1,n2=digitar_n1_n2()
            print(f"{n1} / {n2} =",divisao(n1,n2))
            pause()
        elif aux == 5:
            num=digitar_num()
            print(f"{num}² =",quadrado(num))
            pause()
        elif aux == 6:
            n1,n2=digitar_n1_n2()
            print(f"{n1}^{n2} =",potencia(n1,n2))
            pause()
        elif aux == 7:
            num=digitar_num()
            print(f"√{num} =",raiz(num))
            pause()
        elif aux == 8:
            num=digitar_num()
            print(f"Exponencial de {num} (E^{num}) =",exponencial(num))
            pause()
        elif aux == 9:
            n1,n2=digitar_n1_n2()
            print(f"Log de {n1} na base {n2} =",logaritmo(n1,n2))
            pause()
        elif aux == 10:
            num=digitar_num()
            print(f"Seno({num}) =",seno(num))
            pause()
        elif aux == 11:
            num=digitar_num()
            print(f"Cosseno({num}) =",cosseno(num))
            pause()
        elif aux == 12:
            num=digitar_num()
            print(f"Tangente({num}) =",tangente(num))
            pause()
        elif aux == 13:
            num=digitar_num_1()
            print(f"Seno⁻¹({num}) =",seno_inverso(num))
            pause()
        elif aux == 14:
            num=digitar_num_1()
            print(f"Cosseno⁻¹({num}) =",cosseno_inverso(num))
            pause()
        elif aux == 15:
            num=digitar_num()
            print(f"Tangente⁻¹({num}) =",tangente_inverso(num))
            pause()
        elif aux == 16:
            num=round(float(input("Digite um número inteiro: ")))
            print(f"Fatorial de {num} =",fatorial(num))
            pause()


