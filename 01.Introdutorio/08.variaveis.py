# Interpretador do Python possui tipagem dinâmica:
# O tipo de uma variável é determinado em run time, não em tempo de compilação
var_teste = 1
print(f"var_teste = {var_teste}")

var_teste = 2
print(f"var_teste = {var_teste}")
print(type(var_teste))

var_teste = 9.5
print(f"var_teste = {var_teste}")
print(type(var_teste))

# Declaração múltipla
pessoa1, pessoa2, pessoa3 = "João", "Jorge", "Gustavo"
print(f"Pessoa 1 = {pessoa1}")
print(f"Pessoa 2 = {pessoa2}")
print(f"Pessoa 3 = {pessoa3}")

fruta1 = fruta2 = fruta3 = "Melância"
print(f"Fruta 1 = {fruta1}")
print(f"Fruta 2 = {fruta2}")
# Python é case-sensitive, não foi criado a variável 'Fruta2', logo gerará erro
#print(f"Fruta 1 = {Fruta2}")
print(f"Fruta 3 = {fruta3}")

x1=50
print(x1)

# Python não permite nomes de variáveis que iniciem com números
#1x=50

# Não se pode usar palavras reservadas como nome de variável:
#and                as              assert              break
#class              continue        def                 del
#elif               else            except              False
#finally            for             from                global
#if                 import          in                  is
#lambda             None            nonlocal            not
#or                 pass            raise               return
#True               try             while               with
#yield

largura = 2
altura = 4
area = largura * altura
print(f"Área: {area}")
perimetro = 2 * largura + 2 * altura
print(f"Perímetro: {perimetro}")
# A ordem dos operadores é a mesma seguida na Matemática
perimetro = 2 * (largura + 2) * altura
print(f"Perímetro (sic): {perimetro}")

# Operações com variáveis
idade1 = 25
idade2 = 35
print(f"idade1 + idade2 = {idade1+idade2}")
print(f"idade1 - idade2 = {idade1-idade2}")
print(f"idade1 * idade2 = {idade1*idade2}")
print(f"idade1 / idade2 = {idade1/idade2}")
print(f"idade1 % idade2 = {idade1%idade2}")

# Concatenação de Variáveis
nome = "Gustavo"
sobrenome = "Borges"
fullName = nome + " " + sobrenome
print(fullName)