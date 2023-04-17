posiblePrimo = int(input("Introduzca un número primo: "))
primo = True
numero = posiblePrimo - 1
while numero >= 2:
    if posiblePrimo % numero == 0:
        primo = False
        break
    else:
        numero -= 1
if primo == True:
    resultado = f"El número {posiblePrimo} es primo"
else:
    resultado = f"El número {posiblePrimo} no es primo, pues {numero} es un divisor del mismo"
print(resultado)