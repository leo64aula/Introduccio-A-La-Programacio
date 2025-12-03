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
    logging.debug(f"El resultat de la suma de {num1} + {num2} es igual a {suma}")
    logging.debug(f"El resultat de la resta de {num1} + {num2} es igual a {resta}")
    logging.debug(f"El resultat de la multiplicacio de {num1} + {num2} es igual a {multiplicacio}")
    logging.debug(f"El resultat de la divisio de {num1} + {num2} es igual a {divisio}")
except ZeroDivisionError:
    logging.debug("El numero 0 no es pot dividir, proba un altre")
except ValueError:
    logging.debug("Soles pots ficar numeros enters")
