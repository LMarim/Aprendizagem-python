import random
import os
import time

sorteado = random.randint(1,100)
tentativa = 0

while True:
    time.sleep(1)
    os.system('cls')
    numero = int(input('Digite um número entre 1 á 100: '))
    tentativa += 1
    
    if numero == sorteado:
        print(f"Parabéns você acertou em incriveis: {tentativa} tentativas")
        break
    elif numero > sorteado:
        print('O número Digitado é MAIOR que o número misterioso')
    else:
        print('O número Digitado é MENOR que o número misterioso')
    

