# https://docs.python.org/3/library/exceptions.html

def askint():
    try:
        val = int(input("Digite um número: "))
    except:
        print("Você não digitou um número!")
    finally:
        print("Obrigado!")

askint()

def askint():
    try:
        val = int(input("Digite um número: "))
    except:
        print("Você não digitou um número!")
        val = int(input("Tente novamente. Digite um número: "))
    finally:
        print("Obrigado!")
    print(val)

askint()

def askint():
    val = None
    while True:
        try:
            val = int(input("Digite um número: "))
        except:
            print("Você não digitou um número!")
            continue
        else:
            print("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
            if val is not None:
                print(val)

askint()