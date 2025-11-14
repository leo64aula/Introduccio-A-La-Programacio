print("=" * 50)
print("EJERCICIO 3.3 - FUNCIÓN CON VALOR POR DEFECTO")
print("=" * 50)

def sumar(a, b=10):
    """Función que suma dos números. El segundo tiene valor por defecto 10"""
    return a + b

num1 = float(input("Introduce el primer número: "))
respuesta = input("¿Quieres introducir un segundo número? (s/n): ").lower()
if respuesta == 's':
    num2 = float(input("Introduce el segundo número: "))
    resultado = sumar(num1, num2)
    print(f"Suma de {num1} + {num2} = {resultado}")
else:
    resultado = sumar(num1)
    print(f"Suma de {num1} + 10.0 (valor por defecto) = {resultado}")