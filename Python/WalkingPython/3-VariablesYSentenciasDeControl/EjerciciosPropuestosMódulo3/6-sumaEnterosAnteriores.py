"""
6. Crea un programa que le pida al usuario un número entero y luego calcule 
y muestre la suma de todos los números desde 1 hasta el número ingresado.
El programa debe utilizar un bucle `for` para sumar los números.
"""
try:
    numero = int(input("Introduzca un número entero: "))
    suma = 0
    for i in range(1, numero+1):
        suma += i
except Exception as e:
    print(f"Se ha producido el error: \n{e} \n Porque no ha introducido un número entero")
else:
    print(f"La suma de todos los números desde 1 hasta {numero} es {suma}")