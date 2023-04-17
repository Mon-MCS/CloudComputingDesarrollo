numero = input("Introduzca un número entero: ")
numeroInverso = ""
n = len(numero)-1
while n >= 0:
    numeroInverso += numero[n]
    n -= 1
if numero == numeroInverso:
    resultado = f"El número introducido {numero} es capicúa"
else:
    resultado = f"El número introducido {numero} no es capicúa"
print(resultado)
