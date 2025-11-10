print("=" * 50)
print("EJERCICIO 3.2 - ÁREA DE UN CÍRCULO")
print("=" * 50)
def calcular_area_circulo(radio):

    pi = 3.14159
    area = pi * (radio ** 2)
    return area

radio_usuario = float(input("Introduce el radio del círculo: "))
area_calculada = calcular_area_circulo(radio_usuario)
print(f"El área del círculo con radio {radio_usuario} es: {area_calculada:.2f}")