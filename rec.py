import time

tempo = 1;

def sauda ():
    print ("Olá Boa Noite")
    nome = input ("Digite seu nome:")

    print("Bem vindo,", nome + "!")

time.sleep(tempo)

print("O que gostaria?")
"""
Sou o Cadu
Eu amo motos
muito muito
"""

def menu():
    print("1-Revisão")
    print("2-Pintura")
    print("3-Troca de Pneu")
    print("4-Outros")
    opcao = int(input("Digite o numero da opção escolhida:"))

    time.sleep(tempo)
  
    if opcao == 1: 
        print("R$ 100,00")

    elif opcao == 2:
        print("De R$ 200,00 a R$ 600,00 A Variar Do Modelo da Moto ")

    elif opcao == 3:
        print("De $120,00 a R$400,00 ")

    elif opcao == 4:
        print("Visite Nossa Loja Na Roque Vernalha NMR 17")

    else:
        print("Volte ao inicio")

sauda()
menu()
