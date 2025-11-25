temperatura=int(input("Quina temperatura fa en graus celsius? "))
nuvols=str(input("Esta nuvolat? "))
if temperatura < 0:
    print("fa un fred polar")
if temperatura >= 0 and temperatura <= 15:
    if nuvols == "si":
        print("Fa fred i el dia esta trist")
    if nuvols == "no":
        print("Fa fresqueta pero el sl alegra el dia")
if temperatura >= 16 and temperatura <= 25:
    if nuvols == "si":
        print("Temperatura agradable pero pot ser que ploga")
    if nuvols == "no":
        print("Dia perfecte per a ixir a passejar")
if temperatura >= 26 and temperatura <= 35:
    print("Fa calor, millor buscar ombra")
if temperatura > 35:
    if nuvols == "si":
        print("Calor i humitat... una combinacio infernal")
    if nuvols == "no":
        print("Fa una calor que fon les pedres")