idade = 18
if idade > 17:
    print("Você pode tirar sua CNH!")

nome = "Bob"
if idade > 13:
    if nome == "Bob":
        print("Ok Bob, você está autorizado a entrar!")
    else:
        print("Desculpe, mas você não pode entrar!")

idade = 13
nome = "Bob"
if idade >= 13 and nome == "Bob":
    print("Ok Bob, você está autorizado a entrar!")

idade = 12
nome = "Bob"
if (idade >= 13) or (nome == "Bob"):
    print("Ok Bob, você está autorizado a entrar!")