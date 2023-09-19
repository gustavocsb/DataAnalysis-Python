def primeiraFunc():
    print("Hello World!")

#primeiraFunc()

def primeiraFunc():
    nome = "Bob"
    print(f"Hello {nome}!")

#primeiraFunc()

def segundaFunc(nome):
    print(f"Hello {nome}!")

#segundaFunc("Bob")

def imprimeNumeros():
    for i in range(0,5):
        print(f"Número {i}")

#imprimeNumeros()

def addNum(firstNum, secondNum):
    print(f"Primeiro número:  {firstNum}")
    print(f"Segundo número:  {secondNum}")
    print(f"Soma: {firstNum+secondNum}")

#addNum(4,7)

def printVarInfo(arg1, *vartuple):
    print(f"O parâmetro passado foi: {arg1}")

    for item in vartuple:
        print(f"O parâmetro passado foi: {item}")
    return

#printVarInfo(10)
#printVarInfo(10,(10,5,2,3,4,"Teste"))
#printVarInfo(10,"Chocolate",15,"Tupla")