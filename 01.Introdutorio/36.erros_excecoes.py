# SyntaxError: unterminated string literal (detected at line 2)
#print('Hello)
      
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
#8 + 's'

def numDiv(num1, num2):
    resultado = num1 / num2
    print(resultado)

numDiv(4,2) 

# ZeroDivisionError: division by zero
#numDiv(4,0)

'''
  _____                  _                                        _           
 |_   _|  _ __    __ _  | |_    __ _   _ __ ___     ___   _ __   | |_    ___  
   | |   | '__|  / _` | | __|  / _` | | '_ ` _ \   / _ \ | '_ \  | __|  / _ \ 
   | |   | |    | (_| | | |_  | (_| | | | | | | | |  __/ | | | | | |_  | (_) |
   |_|   |_|     \__,_|  \__|  \__,_| |_| |_| |_|  \___| |_| |_|  \__|  \___/ 

      _        
   __| |   ___ 
  / _` |  / _ \
 | (_| | |  __/
  \__,_|  \___|
                                                   
  _____                             
 | ____|  _ __   _ __    ___    ___ 
 |  _|   | '__| | '__|  / _ \  / __|
 | |___  | |    | |    | (_) | \__ \
 |_____| |_|    |_|     \___/  |___/

'''                                    
# Utilizando try e except
try:
    8 + 's'
except TypeError:
    print("Operação não permitida")

# Utilizando try, except e else
try:
    f = open(r"01.Introdutorio\29.Manipulacao_arquivos\arquivos\testandoerros.txt", "w")
    f.write("Gravando no arquivo")
except IOError:
    print("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
    print("Conteúdo gravado com sucesso!")
    f.close()

# Tentando abrir o arquivo sem a extensão ".txt"
try:
    f = open(r"01.Introdutorio\29.Manipulacao_arquivos\arquivos\testandoerros", "r")
except IOError:
    print("Erro: arquivo não encontrado ou não pode ser lido.")  
else:
    print("Conteúdo gravado com sucesso!")
    f.close()                


# Utilizando try, except, else e finally
try:
    f = open(r"01.Introdutorio\29.Manipulacao_arquivos\arquivos\testandoerros.txt", "w")
    f.write("Gravando strings no arquivo, testando erros")
except IOError:
    print("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
    print("Conteúdo gravado com sucesso!")
    f.close()
finally:
    print("Quaisquer comandos no bloco finally são sempre executados!") 


# **********************************************************************************************************************************************
# * CADA POSSIBILIDADE DE ERRO DEVE SER TRATADA NO PROGRAMA                                                                                    *
# **********************************************************************************************************************************************