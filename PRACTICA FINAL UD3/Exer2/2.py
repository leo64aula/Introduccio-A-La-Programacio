Archiu1 = './Fitxers/Hola.txt'
Archiu2 = './Fitxers/Alberto.txt'
Archiu3 = './Fitxers/HOLAALBERTO.txt'

try:
    with open(Archiu1, 'r') as fitxer1:
        contingut1 = fitxer1.read()
        contingut3 = contingut1 

    with open(Archiu2, 'r') as fitxer2:
        contingut2 = fitxer2.read()
        contingut3 = contingut3 + " " + contingut2
    
    with open(Archiu3,'w') as fitxer3:
        fitxer3.write(f"La concatenació dels arxius es: {contingut3}")

    print("El contenido de ambos ficheros es:")
    print(contingut3)

except FileNotFoundError:
    print(f"Error: No se encontró uno de los archivos especificados.")