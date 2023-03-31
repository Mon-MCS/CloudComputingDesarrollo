año = int(input("Introduza el año que desea saber si es bisiesto: "))
if (año % 4 == 0) and (año % 100 != 0):
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")