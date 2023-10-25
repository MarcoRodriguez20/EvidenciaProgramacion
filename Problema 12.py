ventas_tortas = 0
ventas_tacos = 0
ventas_hotdogs = 0
ventas_pizzas = 0

n = int(input("Ingrese la cantidad de alumnos atendidos: "))

for i in range(n):
    print(f"Alumno {i + 1}:")
    print("1. Torta")
    print("2. Tacos")
    print("3. Hotdogs")
    print("4. Pizzas")
    
    opcion = int(input("Elija el número de producto que desea comprar (1-4): "))
    
    if opcion == 1:
        ventas_tortas += 1
    elif opcion == 2:
        ventas_tacos += 1
    elif opcion == 3:
        ventas_hotdogs += 1
    elif opcion == 4:
        ventas_pizzas += 1
    else:
        print("Opción no válida. Por favor, elija un número de producto válido.")

print("Resumen de ventas:")
print(f"Tortas vendidas: {ventas_tortas}")
print(f"Tacos vendidos: {ventas_tacos}")
print(f"Hotdogs vendidos: {ventas_hotdogs}")
print(f"Pizzas vendidas: {ventas_pizzas}")