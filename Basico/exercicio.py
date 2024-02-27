import os

nome = input('Digite o seu nome: ')
os.system('clear')

valor01 = float(input("Digite o primeiro número: "))
valor02 = float(input("Digite o segundo número: "))
#valor03 = float(input("Digite o terceiro número: "))
os.system('clear')

calculo = valor01 * valor02

print(f'O resultado do seu calculo,{nome}, é igual a = {calculo:.0f}')

#os.system('shutdown /s')