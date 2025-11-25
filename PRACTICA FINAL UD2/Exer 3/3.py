numero= int(input("Disme un numero "))
positius= 0
while numero != 0:
    if numero > 0:
        positius= positius + 1
    numero= int(input("Fica un altre numero "))
print(positius)