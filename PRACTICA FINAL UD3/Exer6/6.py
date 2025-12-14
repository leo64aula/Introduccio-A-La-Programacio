import json

try:
    with open('dades_exercici6.json', 'r') as fitxer:
        dades = json.load(fitxer)

    dades[1]["assignatures"].append("Carlitos Subiela")

    with open('dades_exercici6.json', 'w') as fitxer:
        json.dump(dades, fitxer, indent=4)
    
    print("Asignatura añadida.")

except FileNotFoundError:
    print("No s'ha trobat l'arxiu")
except IndexError:
    print("El archivo JSON está vacío o no tiene el formato esperado.")