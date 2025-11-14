print("=" * 50)
print("EJERCICIO 4.2 - OPERADOR IN Y NOT IN")
print("=" * 50)

frutas = ["mango", "arandano", "plátano", "naranja", "kiwi"]
print(f"Lista de frutas: {frutas}")

fruta_buscar = input("\nIntroduce el nombre de una fruta: ").lower()

if fruta_buscar in frutas:
    print(f"¡Sí! {fruta_buscar} está en la lista.")
else:
    print(f"No, {fruta_buscar} no está en la lista.")