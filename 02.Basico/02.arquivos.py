#
#  __  __                   _                   _                       _         
# |  \/  |   __ _   _ __   (_)  _ __    _   _  | |   __ _   _ __     __| |   ___  
# | |\/| |  / _` | | '_ \  | | | '_ \  | | | | | |  / _` | | '_ \   / _` |  / _ \ 
# | |  | | | (_| | | | | | | | | |_) | | |_| | | | | (_| | | | | | | (_| | | (_) |
# |_|  |_|  \__,_| |_| |_| |_| | .__/   \__,_| |_|  \__,_| |_| |_|  \__,_|  \___/ 
#                              |_|
#     _                             _                       
#    / \     _ __    __ _   _   _  (_) __   __   ___    ___ 
#   / _ \   | '__|  / _` | | | | | | | \ \ / /  / _ \  / __|
#  / ___ \  | |    | (_| | | |_| | | |  \ V /  | (_) | \__ \
# /_/   \_\ |_|     \__, |  \__,_| |_|   \_/    \___/  |___/
#                      |_|

import os
import numpy as np
file_name = os.path.join('02.Basico', 'dataset.csv')

# '!more dataset.csv' no Jupyter Notebook o prefixo '!' executa comandos do sistema operacional
# Replicando em python:
#arquivo = os.path.join('02.Basico', 'dataset.csv')

#os.system('more ' + arquivo) # Comando 'more' em windows é um paginador que exibe o conteúdo do arquivo no console
#os.system('type ' + arquivo) # Comando 'type' em windows exibe todo o conteúdo do arquivo no console

# Abrindo o arquivo diretamente com python:
# with open('02.Basico/dataset.csv', 'r') as file:
#     for line in file:
#         print(line)

# Carregando o dataset dentro de um array com numpy
file = np.loadtxt(file_name, delimiter=',', usecols=(0, 1, 2, 3), skiprows=1)
print(file)
print(f'Type: {type(file)}')

# Carregando apenas duas variáveis (colunas) do dataset
var1, var2 = np.loadtxt(file_name, delimiter=',', usecols=(0, 1), skiprows=1, unpack=True)

# Gerando um plot a partir de um arquivo usando o matplotlib:

import matplotlib.pyplot as plt # Importando a biblioteca matplotlib

plt.plot(var1,var2, 'o', markersize=6,color='blue') # Criando um gráfico de dispersão com a função 'plot'
plt.show() # Exibindo o gráfico com a função 'show'
