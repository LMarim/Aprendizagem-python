import os

nome = input('Digite o seu nome: ')
os.system('clear')
uni1 = float(input('Digite a sua nota da 1ª Unidade: '))
uni2 = float(input('Digite a sua nota da 2ª Unidade: '))
uni3 = float(input('Digite a sua nota da 3ª Unidade: '))
os.system('clear')

media = (uni1+uni2+uni3)/3

if media >= 7:
    print(f"Aluno {nome}, sua média foi: {media:.1f} e você foi aprovado.")
elif media>=5 and media <7:
    print(f"Aluno {nome}, sua média foi: {media:.1f} e você foi para a prova final.")
else:
    print(f"Aluno {nome}, sua média foi: {media:.1f} e você foi para recuperação.")
    