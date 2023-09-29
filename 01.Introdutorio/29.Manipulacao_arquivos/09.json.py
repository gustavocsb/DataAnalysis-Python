# JSON (Java Script Object Notation), é um formato de texto, similar ao .txt e .csv, é baseado em uma estrutura de objetos JavaScript e usa pares
# de chave-valor para representar dados. JSON é facilmente lido e escrito por máquinas e é amplamente utilizado como formato de intercâmbio de
# dados em aplicações web modernas

dict_guido = {'nome': 'Guido van Rossum',
              'linguagem': 'Python',
              'similar': ['c', 'Modula-3', 'lisp'],
              'users':1000000}

for k,v in dict_guido.items():
    print(k,v)

import json

# Convertendo o dicionário para um objeto json
print(json.dumps(dict_guido))

# Criando um arquivo JSON
with open(r'01.Introdutorio\Manipulacao_arquivos\arquivos\dados2.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict_guido))

# Leitura de arquivos JSON
with open (r'01.Introdutorio\Manipulacao_arquivos\arquivos\dados2.json', 'r') as arquivo:
    texto = arquivo.read()
    dados2 = json.loads(texto)

print(dados2)
print(dados2['nome'])

# *******************************************************************************************************************

# Extração de Arquivo da Web

# Imprimindo um arquivo JSON copiado da internet
from urllib.request import urlopen

response = urlopen ("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]

print(dados)

print("Título: ",dados['title'])
print("URL: ", dados['url'])
print("Duração: ", dados['duration'])
print("Número de visualizações: ",dados['stats_number_of_plays'])

# Nomes dos arquivos

source_file = r"01.Introdutorio\Manipulacao_arquivos\arquivos\dados2.json"
destiny_file = r"01.Introdutorio\Manipulacao_arquivos\arquivos\dados2.txt"

# Método 1
with open(source_file, 'r') as infile:
    text = infile.read()
    with open(destiny_file, 'w') as outfile:
        outfile.write(text)

# Método 2
open(destiny_file, 'w').write(open(source_file, 'r').read())

print(dados2)