print("=" * 50)
print("EJERCICIO 5.1 - CALCULADORA DE IMC")
print("=" * 50)
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en Metros: "))
imc = peso / (altura ** 2)
print(f"\nTu IMC es: {imc:.2f}")
if imc < 18.5:
    print("Tu IMC está por debajo del peso saludable.")
elif 18.5 <= imc <= 24.9:
    print("¡Felicidades! Tu IMC está en un rango saludable.")
else:
    print("Caaaabroonn, ni el puto CARLOS tiene esos stats.")