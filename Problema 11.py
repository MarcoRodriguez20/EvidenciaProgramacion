numero_dia = int(input("Ingrese un número del 1 al 7: "))

if numero_dia == 1:
    dia_semana = "Lunes"
elif numero_dia == 2:
    dia_semana = "Martes"
elif numero_dia == 3:
    dia_semana = "Miércoles"
elif numero_dia == 4:
    dia_semana = "Jueves"
elif numero_dia == 5:
    dia_semana = "Viernes"
elif numero_dia == 6:
    dia_semana = "Sábado"
elif numero_dia == 7:
    dia_semana = "Domingo"
else:
    dia_semana = "Día no válido"

print(f"El día número {numero_dia} corresponde a {dia_semana}.")
