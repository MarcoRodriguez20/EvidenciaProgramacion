n = int(input("Ingrese la cantidad de números que desea sumar sus cuadrados: "))

suma_cuadrados = 0

for i in range(n):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    cuadrado = numero ** 2
    suma_cuadrados += cuadrado

print(f"La suma de los cuadrados de los {n} números es: {suma_cuadrados}")
