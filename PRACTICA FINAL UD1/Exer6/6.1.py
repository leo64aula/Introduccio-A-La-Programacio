a = [5, 10, 15]
b = 20

if 5 in a:
    b -= 5
if 10 in a:
    b -= 10
if 15 in a:
    b -= 15

print(b)
#Hola Alberto, aquest codi, es simple, primer defineix les variables, on "a" te una llista amb distints valors y "b" soles té el valor 20.
#Despres hi han varios if independents, el if comprova si els valors (5, 10 y 15) estan en "a".
#Cada uno fa una resta y cambia el valor de b progresivament en el cas que el if siga correcte.
#Al acabar totes les operacions, fem un print del resultat final despres de passar per totes les operacions, i comprovem que el resultat es -10
#20 -5 = 15     15 - 10 = 5      5 - 15 = -10
