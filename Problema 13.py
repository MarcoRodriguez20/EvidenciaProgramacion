def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Elija el número de operación que desea realizar (1-4): ")

if opcion == 1:
    resultado = suma(numero1, numero2)
elif opcion == 2:
    resultado = resta(numero1, numero2)
elif opcion == 3:
    resultado = multiplicacion(numero1, numero2)
elif opcion == 4:
    resultado = division(numero1, numero2)
else:
    resultado = "Opción no válida"

print(f"Resultado: {resultado}")
