import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filename= 'operacions.log',
    filemode='w'
)
try:
    num1= int(input("Disme el primer numero: "))
    num2= int(input("Disme el segon numero: "))
    suma= num1 + num2
    resta= num1 - num2
    multiplicacio= num1 * num2 
    divisio= num1 / num2
    print(f"El resultat de la suma de {num1} + {num2} es igual a {suma}")
    print(f"El resultat de la resta de {num1} + {num2} es igual a {resta}")
    print(f"El resultat de la multiplicacio de {num1} + {num2} es igual a {multiplicacio}")
    print(f"El resultat de la divisio de {num1} + {num2} es igual a {divisio}")
except ZeroDivisionError:
    print("El numero 0 no es pot dividir, proba un altre")
except ValueError:
    print("Soles pots ficar numeros enters")
