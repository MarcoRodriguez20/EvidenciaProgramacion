n = int(input("Ingrese la cantidad de números a promediar: "))

suma = 0

for i in range(n):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    while numero <= 0:
        
        print("El número debe ser positivo. Inténtelo de nuevo.")
        numero = float(input(f"Ingrese el número {i + 1}: "))
    suma += numero

promedio = suma / n

print(f"El promedio de los {n} números positivos es: {promedio}")
