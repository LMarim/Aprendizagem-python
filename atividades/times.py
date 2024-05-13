import os

times = [
    
    "Bayern de Munique",
    "Borussia dortmud",
    "Leipzig",
    "Barcelona",
    "Real Madrid",
    "Atlético de Madrid",
    "Real Sociedad",
    "Manchester City",
    "Arsenal",
    "Inter de Milhão",
    "Napoli",
    "PSG",
    "Porto",
    "Copenhague",
    "PSV",
    "Lazio"
    
]

print('Bem vindo ao Jogo da Adivinhação')
print('Tente adivinhar - 3 times da Champions League!')

def jogo(times):
    
    pontos = 0
    
    for x in range(3):
        palpite = input('Digite um time: ').capitalize().strip()
        
        if palpite in times:
            pontos+= 1
            os.system('cls')
            print(f"Parábens você acertou o time, você tem {pontos} pontos!")
            times.remove(palpite)
        else:
            os.system('cls')
            print(f"Este time não está na lista,você tem {pontos} pontos!")
            
jogo(times)