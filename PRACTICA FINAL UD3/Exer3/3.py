# 1 Creació i Escriptura
with open('./Fitxers/prueba.txt', 'w') as fitxer:
    fitxer.write(f"Primera línia")
    fitxer.write("\n")

with open('./Fitxers/prueba.txt', 'w') as fitxer:
    fitxer.write(f"Segona línia")
    fitxer.write("\n")
# Primer es crea el archiu ya que no existeix, despres s'escriu "Primera linea", despres es sobrescriu el archiu pq ya esta creat amb el text Segona Linia
# 2 Creació i Exclusiva
# with open('./Fitxers/prueba.txt', 'x') as fitxer:
#         fitxer.write(f"Tercera línia")
# Al fer aso me ix un error de que el fitxer ja existeix i si borre passa el mateix a no ser que comente o borre el primer exercici
# 3 Afegir al Final
with open('./Fitxers/prueba.txt', 'a') as fitxer:
    fitxer.write(f"Quarta línia")
    fitxer.write("\n")
with open('./Fitxers/prueba.txt', 'a') as fitxer:
    fitxer.write(f"Cinquena línia")
    fitxer.write("\n")
    fitxer.write(f"Sisena línia")
    fitxer.write("\n")
with open('./Fitxers/prueba.txt', 'r') as fitxer:
    contingut = fitxer.read()
    print(contingut)
# 4 Llegir i Tancar Fitxers
with open('./Fitxers/prueba.txt', 'r') as fitxer:
    contingut = fitxer.read()
    print(contingut)
    fitxer.close()
with open('./Fitxers/proba.txt', 'r') as fitxer:
    contingut = fitxer.read()
    print(contingut)
# Ix el error FileNotFoundError.
