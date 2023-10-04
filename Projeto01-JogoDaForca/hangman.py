import random
from os import system, name
from bs4 import BeautifulSoup
import requests

def limpar_tela():
    if name == 'nt':
        # ' _ ' convenção comum em Python para indicar que uma variável é descartável e não será usado mais tarde, visto que a função system retorna valor
        _ = system('cls')
    else:
        _ = system('clear')

def get_VerdurasLegumes(url):
    #resposta = requests.get(url)
    #soup = BeautifulSoup(resposta.text, 'html.parser')
    #elementos = soup.find_all('td')

    elementos = BeautifulSoup(requests.get(url).text, 'html.parser').find_all('td')
    
    palavras = []

    for i in range(0, len(elementos), 4):
        palavras_legumes = [p.text for p in elementos[i+1].find_all('p')]
        palavras_verduras = [p.text for p in elementos[i+2].find_all('p')]
        
        for palavra in palavras_legumes + palavras_verduras:
            if ' (' in palavra and ')' in palavra:
                palavra_sem_parenteses = palavra.replace('(', '').replace(')', '')
                palavras.extend(palavra_sem_parenteses.split(' '))
            else:
                palavras.append(palavra)

    return palavras

def get_Frutas(url):
    #resposta = requests.get(url)
    #soup = BeautifulSoup(resposta.text, 'html.parser')
    #elementos = soup.find_all('h2')
    
    elementos = BeautifulSoup(requests.get(url).text, 'html.parser').find_all('h2')
    
    palavras = []

    for i in range(len(elementos)):
        if 'Fruta com' in elementos[i].text:
            palavras_f = [li.text for li in elementos[i].find_next('ul').find_all('li')]
            palavras.extend(palavras_f)

    return palavras

verdurasLegumes = get_VerdurasLegumes('https://www.dicio.com.br/lista-de-legumes-e-verduras-de-a-a-z/')
frutas = get_Frutas('https://www.dicio.com.br/frutas-de-a-a-z/')

FVL_hard = frutas + verdurasLegumes
FVL_easy = list(filter(lambda x: len(x) < 9, FVL_hard))

def get_Filmes(url):
    elementos = BeautifulSoup(requests.get(url).text, 'html.parser').find_all('h3', class_='lister-item-header')

    palavras = []

    for elemento in elementos:
        palavras.append(elemento.find('a').text)

    return palavras

filmes_hard = get_Filmes('https://www.imdb.com/list/ls002206094/')
filmes_easy = list(filter(lambda x: len(x) < 11, filmes_hard))

def get_PCH(url):
    elementos = BeautifulSoup(requests.get(url).text, 'html.parser').find_all('h2')

    palavras = []

    for elemento in elementos:
        ul = elemento.find_next('ul')
        if ul:
            for li in ul.find_all('li'):
                palavra = li.text
                if not any(char.isdigit() for char in palavra):
                    palavra = palavra.split('\n')[0]
                    if len(palavra) > 1 and not palavra.startswith("Lista"):
                        palavras.append(palavra)

    return palavras

pch_hard = get_PCH("https://pt.wikipedia.org/wiki/Lista_de_partes_da_anatomia_humana")
pch_easy = list(filter(lambda x: len(x) < 11, pch_hard))

def get_CP(url):
    print(requests.get(url).text)

    palavras = []

    return palavras

cp_hard = get_CP("https://www.sport-histoire.fr/pt/Geografia/Paises_por_ordem_alfabetica.php")
#cp_easy = list(filter(lambda x: len(x) < 9, cp_hard))
#print(f"CP Hard:\n{cep_hard}\n\n\nCP Easy:\n{cp_easy}")





'''
def hangman():
    limpar_tela()
    print(" _   _                           __  __                 ")
    print("| | | |   __ _   _ __     __ _  |  \/  |   __ _   _ __  ")
    print("| |_| |  / _` | | '_ \   / _` | | |\/| |  / _` | | '_ \ ")
    print("|  _  | | (_| | | | | | | (_| | | |  | | | (_| | | | | |")
    print("|_| |_|  \__,_| |_| |_|  \__, | |_|  |_|  \__,_| |_| |_|")
    print("                         |___/                          ")




hangman()
'''
