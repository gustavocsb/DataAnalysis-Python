# Variável Global
var_global = 10 # Esta é uma variável global

# Função
def multiplica_numeros(num1,num2):
    var_global = num1*num2 # Esta é uma variável local
    print(var_global)

multiplica_numeros(5,25)
print(var_global)

# A variável global está dentro do main, a variável local existe apenas dentro da função

var_global = 10

def multiplica_numeros(num1,num2):
    var_local = num1*num2 # Esta é uma variável local
    print(var_local)

multiplica_numeros(10,6)
# var_local não está definida, visto que só existe dentro da função, um escopo local
#print(var_local)