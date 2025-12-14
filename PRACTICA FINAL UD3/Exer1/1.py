nom = input("Como et diuen? ")
edat = int(input("Cuants anys tens? "))

try:
    with open('dades usuari.txt', 'w') as fitxer:
        fitxer.write(f"Nom: {nom}\n")
        fitxer.write(f"Edat: {edat}\n")

    with open('dades usuari.txt', 'r') as fitxer:
        contingut = fitxer.read()
        print("Contingut del fitxer:")
        print(contingut)

    ciutat = input("On vius? ")
    
    with open('dades usuari.txt', 'a') as fitxer:
        fitxer.write(f"Ciutat: {ciutat}\n")

    with open('dades usuari.txt', 'r') as fitxer:
        contingut = fitxer.read()
        print("Contingut del fitxer:")
        print(contingut)

except FileNotFoundError:
    print('Error: Fitxer no trobat')
except PermissionError:
    print('Error: Acces denegat')
except ValueError:
    print('Error: Introdueix una edat valida')