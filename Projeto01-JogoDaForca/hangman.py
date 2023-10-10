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

def pause():
    input("Aperte ENTER para continuar")

def get_VerdurasLegumes(url):
    elementos = BeautifulSoup(requests.get(url).text, 'html.parser').find_all('td')

    palavras = []

    for i in range(0, len(elementos), 4):
        palavras_legumes = [p.text.lower() for p in elementos[i+1].find_all('p')]
        palavras_verduras = [p.text.lower() for p in elementos[i+2].find_all('p')]
        
        for palavra in palavras_legumes + palavras_verduras:
            if ' (' in palavra and ')' in palavra:
                palavra_sem_parenteses = palavra.replace('(', '').replace(')', '')
                palavras.extend(palavra_sem_parenteses.split(' '))
            else:
                palavras.append(palavra)

    return palavras

def get_Frutas(url):
    elementos = BeautifulSoup(requests.get(url).text, 'html.parser').find_all('h2')

    palavras = []

    for i in range(len(elementos)):
        if 'Fruta com' in elementos[i].text:
            palavras_f = [li.text.lower() for li in elementos[i].find_next('ul').find_all('li')]
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
                palavra = li.text.lower()
                if not any(char.isdigit() for char in palavra):
                    palavra = palavra.split('\n')[0]
                    if len(palavra) > 1 and not palavra.startswith("Lista"):
                        palavras.append(palavra)

    return palavras

pch_hard = get_PCH("https://pt.wikipedia.org/wiki/Lista_de_partes_da_anatomia_humana")
pch_easy = list(filter(lambda x: len(x) < 11, pch_hard))

def get_CidPais(url):
    elementos = BeautifulSoup(requests.get(url).text, 'html.parser').find_all('tr')

    palavras = []

    for elemento in elementos:
        cols = elemento.find_all('td')
        if len(cols) >= 2:
            pais = cols[0].find('a').text.lower()
            capital = cols[1].text.lower()
            palavras.append(pais)
            palavras.append(capital)

    return palavras

CidPais_hard = get_CidPais("https://www.sport-histoire.fr/pt/Geografia/Paises_por_ordem_alfabetica.php")
CidPais_easy = list(filter(lambda x: len(x) < 9, CidPais_hard))

def hangmanDefault(tema):
    palavra = random.choice(tema)
    qtdLetras = [ '_' for letra in palavra]
    chances = len(palavra)
    letras_erradas = []
    letras_usadas = []

    acentos = {
        'a' : 'àáâã',
        'e' : 'èéê',
        'i' : 'ìíî',
        'o' : 'òóôõ',
        'u' : 'ùúû',
        'c' : 'ç'
    }

    while chances > 0:
        limpar_tela()
        print(" ".join(qtdLetras))
        print("\nTentativas restantes:",chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()
        while len(tentativa) != 1 or tentativa in letras_usadas or not tentativa.isalpha:
            if len(tentativa) != 1:
                print("Digite apenas uma letra!")
            elif not tentativa.isalpha():
                print("Por favor, digite apenas letras.")    
            else:
                print("Você já usou essa letra.")
            tentativa = input("\nDigite uma letra: ").lower()

        letras_usadas.append(tentativa)
        for chave, valor in acentos.items():
            if tentativa == chave:
                letras_usadas.extend(list(valor))

        if tentativa in palavra or any(tentativa in acentos[chave] and chave in palavra for chave in acentos):
            i = 0
            for letra in palavra:
                if tentativa == letra or any(tentativa in acentos[chave] and letra == chave for chave in acentos):
                    qtdLetras[i] = letra
                i+=1
        else:
            chances-=1
            letras_erradas.append(tentativa)

        if "_" not in qtdLetras:
                        print("\nVocê venceu!")

    if chances == 0:
        print("\nVocê perdeu! A palavra era:", palavra,"\n")
        pause()
        limpar_tela()


def hangman():
    sair = False

    while sair == False:
        voltar = False
        limpar_tela()
        print(" _   _                           __  __                 ")
        print("| | | |   __ _   _ __     __ _  |  \/  |   __ _   _ __  ")
        print("| |_| |  / _` | | '_ \   / _` | | |\/| |  / _` | | '_ \ ")
        print("|  _  | | (_| | | | | | | (_| | | |  | | | (_| | | | | |")
        print("|_| |_|  \__,_| |_| |_|  \__, | |_|  |_|  \__,_| |_| |_|")
        print("                         |___/                          \n")
        pause()
        print("\nEscolha um tema:\n")
        print("1 - Frutas, Verduras e Legumes   2 - Filmes")
        print("3 - Partes do Corpo Humano       4 - Cidades / Países")
        print("0 - Sair")
        aux = int(input("\nDigite uma opção: "))

        if aux == 0:      
            while True:
                confirmaSaida=input("Tem certeza que deseja sair? (S/N)\n")
                if confirmaSaida.lower() in ["s","n"]:
                    break
                else:
                    print("Letra inválida, responda com 'S' ou 'N' ")
            if confirmaSaida.lower() == "s":
                sair = True

        elif aux == 1:
            while voltar == False:
                print("\n***************************************************")
                print(" _____  __     __  _     ")
                print("|  ___| \ \   / / | |    ")
                print("| |_     \ \ / /  | |    ")
                print("|  _|     \ V /   | |___ ")
                print("|_|        \_/    |_____|\n")
                print("Escolha a dificuldade:\n1 - Hard     2 - Easy\n0 - Voltar")
                dificuldade = int(input("\nDigite uma opção: "))
                if dificuldade == 1:
                    hangmanDefault(FVL_hard)

                elif dificuldade == 2:
                    hangmanDefault(FVL_easy)

                elif dificuldade == 0:
                    voltar = True

                else:
                    print("Número inválido. Digite novamente!") 

        elif aux == 2:
            print("\n***************************************************")
            print(" _____   _   _                          ")
            print("|  ___| (_) | |  _ __ ___     ___   ___ ")
            print("| |_    | | | | | '_ ` _ \\   / _ \\ / __|")
            print("|  _|   | | | | | | | | | | |  __/ \\__ \\")
            print("|_|     |_| |_| |_| |_| |_|  \\___| |___/\n")
                                         
            while voltar == False:
                print("Escolha a dificuldade:\n1 - Hard     2 - Easy\n0 - Voltar")
                dificuldade = int(input("\nDigite uma opção: "))
                if dificuldade == 1:
                    hangmanDefault(filmes_hard)

                elif dificuldade == 2:
                    hangmanDefault(filmes_easy)

                elif dificuldade == 0:
                    voltar = True 

                else:
                    print("Número inválido. Digite novamente!") 

        elif aux == 3:
            print("\n***************************************************")
            print(" ____     ____   _   _ ")
            print("|  _ \   / ___| | | | |")
            print("| |_) | | |     | |_| |")
            print("|  __/  | |___  |  _  |")
            print("|_|      \____| |_| |_|\n")
                        
            while voltar == False:
                print("Escolha a dificuldade:\n1 - Hard     2 - Easy\n0 - Voltar")
                dificuldade = int(input("\nDigite uma opção: "))
                if dificuldade == 1:
                    hangmanDefault(pch_hard)

                elif dificuldade == 2:
                    hangmanDefault(pch_easy)

                elif dificuldade == 0:
                    voltar = True 

                else:
                    print("Número inválido. Digite novamente!") 

        elif aux == 4:
            print("\n***************************************************")
            print("  ____   _       _        __    ____            _       ")
            print(" / ___| (_)   __| |      / /   |  _ \    __ _  (_)  ___ ")
            print("| |     | |  / _` |     / /    | |_) |  / _` | | | / __|")
            print("| |___  | | | (_| |    / /     |  __/  | (_| | | | \__ \\")
            print(" \____| |_|  \__,_|   /_/      |_|      \__,_| |_| |___/ \n")
                                                         
            while voltar == False:
                print("Escolha a dificuldade:\n1 - Hard     2 - Easy\n0 - Voltar")
                dificuldade = int(input("\nDigite uma opção: "))
                if dificuldade == 1:
                    hangmanDefault(CidPais_hard)

                elif dificuldade == 2:
                    hangmanDefault(CidPais_easy)

                elif dificuldade == 0:
                    voltar = True 

                else:
                    print("Número inválido. Digite novamente!") 

        else:
            print("Número inválido. Digite novamente!")


hangman()

