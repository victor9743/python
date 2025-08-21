# bibliotecas

# importando bibliotecas que faz operações matemáticas
import math
# importando biblioteca de data
import datetime
# importando biblioteca random
import random

def calculo_raiz():
    num = int(input("informe um número "))
    print(f"A raiz quandrada de {num} é {math.sqrt(num)}")

def hora_atual():
    print(datetime.datetime.now())

def numero_aleatorio():
    print(random.randint(1,100))
 


while(True):
    print("1 - calculo da raiz quadrada")
    print("2 - hora atual")
    print("3 - número aletório")
    print("outra opção - sair")

    opcao = input("selecione uma opção")

    if opcao == "1":
        calculo_raiz()
    elif opcao == "2":
        hora_atual()
    elif opcao == "3":
        numero_aleatorio()
    else:
        print("FIM")
        break;








