# Em Python, um módulo é um arquivo(script) que contém código Python e pode ser importado em outros arquivos Python. Ele é usado para compartilhar funções,
# classes e variáveis entre arquivos.

# Já um pacote é uma coleção de módulos organizados em uma estrutura de diretórios. Ele permite a divisão de um aplicativo em múltiplos módulos, o que facilita
# a manutenção e o desenvolvimento.

# Repositório de pacotes da Linguagem Python: https://pypi.org/



# Importando um pacote Python
import numpy as np

# Verificando todos os métodos e atributos disponíveis no pacote 
print(dir(np))

# Usando um dos métodos do pacote Numpy
print(np.sqrt(25))

# Importando apenas um dos métodos do pacote Numpy, aloca menos memória
from numpy import sqrt
print(sqrt(9))

# Método help para descrever a função help, parâmetros, exemplos, entrada e saída de dados, etc
#print(help(sqrt))

import random

print(random.choice(["Abacate", "Banana", "Laranja"]))

print(random.sample(range(100),10))

import statistics

dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(dados))
print(statistics.median(dados))

import os

print (os.getcwd())
#print(dir(os))


# Importando o módulo request do pacote urllib, usado para trazer url's para dentro do ambiente Python
import urllib.request

# Variável resposta armazena o objeto de conexão à url passada como parâmetro
resposta = urllib.request.urlopen('http://python.org')
# Objeto resposta
print(resposta)

# Chamando o método read() do objeto resposta e armazenando o código html na variável html
html = resposta.read()
# Imprimindo o HTML do site
#print(html)