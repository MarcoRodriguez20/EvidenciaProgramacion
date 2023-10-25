import random

pares = 0
impares = 0

for _ in range(30):
    numero = random.randint(1, 30)  
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Se generaron 30 números aleatorios.")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
