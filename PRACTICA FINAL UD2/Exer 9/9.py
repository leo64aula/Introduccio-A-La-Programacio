elements= ["poma", "pera", "taronja", "platan"]
seleccio= None
try:
    pos= int(input("Introdueix una posició del 0 al 3: "))
    seleccio= elements[pos]
    print(f"L'element en la posicio {pos} es: {seleccio}")
except ValueError:
    print("Introdueix un numero enter")
except IndexError:
    print("La posició no existeix en la llista")
