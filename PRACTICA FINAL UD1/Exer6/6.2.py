a = [5, 10, 15]
b = 20

if 5 in a:
    b -= 5
elif 10 in a:
    b -= 10
else:
    b -= 15

print(b)

#Buenas, dirte que el codi l'he he tingut que corregir perque estaba mal fet. 
#Aquest codi primer defineix les variables, on "a" te una llista amb distints valors y "b" soles té el valor 20.
#Veguem que despres tenim una estructura de if, elif i else, nem a vore que fa cada una.
#IF: Comprova que el numero 5 estiga dins de la llista de "a" en cas de ser correcte el resultat seria 15 (20 - 5) ahi se acabaria el codi.
#ELIF: Si el if no es correcte pero el numero 10 esta dins de la llista "a" el resultat seria 10  (20 - 10) ahi se acabaria el codi
#ELSE: Si ninguno dels dos es correcte el resultat seria 5 (20 - 15)