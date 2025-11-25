print("=" * 50)
print("EJERCICIO 1.1 - CALCULADORA SIMPLE")
print("=" * 50)
num1 = int(input("Introduce un número entero: "))
num2 = float(input("Introduce un número decimal:"))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
modulo = num1 % num2
print(f"\nResultados:")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")
print(f"División entera: {num1} // {num2} = {division_entera}")
print(f"Módulo: {num1} % {num2} = {modulo}")
mensaje = "El resultado de sumar " + \
    str(num1) + " y " + str(num2) + " es " + str(suma)
print(f"\nConcatenación: {mensaje}")
