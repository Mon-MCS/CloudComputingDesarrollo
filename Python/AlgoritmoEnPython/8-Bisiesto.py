año = int(input("Introduza el año que desea saber si es bisiesto: "))
if (año % 4 == 0) and (año % 100 != 0):
    resultado = f"El año {año} es bisiesto"
elif año % 400 == 0:
    resultado = f"El año {año} es bisiesto"
else:
    resultado = f"El año {año} no es bisiesto"
print(resultado)