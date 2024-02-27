numeros = [5,-3,10,8,-2,15,7,-9,4,6]

Positivo =[]
Negativo = []

for x in numeros:
    if x > 0:
        Positivo.append(x)
    else:
        Negativo.append(x)
        
print(f"Os números positivos são:{Positivo}")    
print(f"Os números negativos são:{Negativo}")    
print(f"Total de números positivos:{len(Positivo)}")    
print(f"Total de números negativo:{len(Negativo)}")    
   
        
