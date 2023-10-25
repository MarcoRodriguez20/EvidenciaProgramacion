n = int(input("Ingrese el número de personas: "))

suma_edades = 0

ano_actual = 2023

for i in range(n):
    ano_nacimiento = int(input(f"Ingrese el año de nacimiento de la persona {i + 1}: "))
    edad = ano_actual - ano_nacimiento
    suma_edades += edad

promedio_edades = suma_edades / n

print(f"La edad promedio de las {n} personas es: {promedio_edades} años")
