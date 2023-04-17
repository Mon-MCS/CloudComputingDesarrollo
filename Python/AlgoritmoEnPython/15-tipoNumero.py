numero = float(input("Introduza un número: "))
if numero > 0:
    resultad0 = f"El número {numero} introducido es positivo"
elif numero < 0:
    resultado = f"El número {numero} introducido es negativo"
else:
    resultado = f"El número {numero} introducido es 0"
print(resultado)