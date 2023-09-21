# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!

#Celsius = [39.2, 36.5, 37.3, 37.8]
#Fahrenheit = map(coloque_aqui_sua_função_lambda)
#print (list(Fahrenheit))

# F = C*1,8 + 32
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: 1.8*x+32, Celsius)
print (list(Fahrenheit))