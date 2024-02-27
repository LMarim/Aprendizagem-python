import os

nome = input('Digite o seu nome: ')
os.system('clear')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
os.system('clear')

imc = peso/(altura**2)

if imc >= 25 and imc <=24.9:
    print(f"{nome}, seu imc é de: {imc:.1f} e você está acima do peso.")
elif imc>=18.5 and imc <25:
    print(f"{nome}, seu imc é de: {imc:.1f} e você está com o peso normal.")
elif imc>=30 and imc <34.9:
    print(f"{nome}, seu imc é de: {imc:.1f} Obesidade grau I.")
elif imc>= 35 and imc <40:
    print(f"{nome}, seu imc é de: {imc:.1f} Obesidade grau II")
elif imc >= 40:
    print(f"{nome}, seu imc é de: {imc:.1f} Obesidade grau III")
elif imc >= 17 and imc<=18.4:
    print(f"{nome}, seu imc é de: {imc:.1f} Abaixo do peso")
elif imc <17:
    print(f"{nome}, seu imc é de: {imc:.1f} Muito abaixo do peso")
    