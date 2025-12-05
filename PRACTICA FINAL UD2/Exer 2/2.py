# Programa amb errors: classifica alumnes per edat i assistència
print("Classificador d'alumnes per edat i assistència")

n = int(input("Quants alumnes vols processar? "))
i = 0

while i < n:
    nom = str(input("Nom: "))
    edat = int(input("Edat: "))
    assist = str(input("Assistència (S/N): ")).lower()

    if edat < 12:
        categoria = "infantil"
    elif edat >= 12 and edat <= 18:
        categoria = "adolescent"
    elif edat >= 18 and edat <= 65:
        categoria = "adult"
    else:
        categoria = "jubilat"

    if assist == "s" or "si":
        estat = "present"
    if assist == "n" or "no":
        estat = "absent"

    print(nom, "-", categoria, "-", estat)
    i = i + 1
