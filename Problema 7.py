n = int(input("Ingrese la cantidad de números a procesar: "))

suma_cuadrados_pares = 0
suma_cubos_impares = 0

for i in range(n):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero % 2 == 0:
        cuadrado = numero ** 2
        suma_cuadrados_pares += cuadrado
    else:
        cubo = numero ** 3
        suma_cubos_impares += cubo

print(f"La suma de los cuadrados de los números pares es: {suma_cuadrados_pares}")
print(f"La suma de los cubos de los números impares es: {suma_cubos_impares}")
