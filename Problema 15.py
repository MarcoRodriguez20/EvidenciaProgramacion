# Solicita al usuario ingresar un número
numero = int(input("Ingrese un número: "))

# Verifica si el número es par o impar
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")
