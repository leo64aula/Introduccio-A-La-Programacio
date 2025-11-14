print("=" * 50)
print("EJERCICIO 1.2 - COMPARAR DOS NÚMEROS")
print("=" * 50)
num_a = float(input("Introduce el primer número: "))
num_b = float(input("Introduce el segundo número: "))
if num_a > num_b:
    print(f"{num_a} es mayor que {num_b}")
elif num_a == num_b:
    print(f"{num_a} es igual a {num_b}")
else:
    print(f"{num_a} es menor que {num_b}")