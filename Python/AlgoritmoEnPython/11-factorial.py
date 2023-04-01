numero = int(input("Introduzca un entero al que calcular el factorial: "))
i = numero
factorial = 1
while i > 1:
    factorial = factorial * i
    i = i-1
print(f"El factorial de {numero} es {factorial}") 