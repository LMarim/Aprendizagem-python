import os

nome = input("Digite o seu nome: ")
os.system('cls')
peso = float(input("Digite o seu peso: "))
os.system('cls')
altura = float(input("Digite a sua altura: "))
os.system('cls')

imc= peso/(altura**2)

print(f'{nome}, imc é: {imc:.1f}')