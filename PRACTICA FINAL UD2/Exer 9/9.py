elements= ["poma", "pera", "taronja", "platan"]
seleccio= None
try:
    pos= int(input("Introdueix una posició del 0 al 3 y te dire a quina fruta correspon: "))
    seleccio= elements[pos]
    print(f"L'element en la posicio {pos} es: {seleccio}")
except ValueError:
    print("Introdueix un numero enter")
except IndexError:
    print("La posició no existeix en la llista")
finally:
    print("Intent Completat")
    print(f"La longitud de la llista es: {len(elements)}")
    seleccio= None
    print("La variable seleccio a segut reiniciada a None")