valores = [22,33,44,23,26,29,67,56,45,46,32,11,17]

Impar = []
Par = []

for x in valores:
    if x % 2 == 0:
        Par.append(x)
    else:
        Impar.append(x)
        


print(f"Números impares: {Impar}")
print(f"Números pares: {Par}")
print(f"Soma dos números: {sum(valores)}")
print(f"Média dos números: {sum(valores)/len(valores):.1f}")