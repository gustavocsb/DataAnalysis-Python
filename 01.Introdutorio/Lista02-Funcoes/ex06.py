# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total # Variável existente apenas dentro do escopo da função

soma( 10, 20 ) # Variável existente em todo o código, global
print ("Fora da função o total é: ", total)