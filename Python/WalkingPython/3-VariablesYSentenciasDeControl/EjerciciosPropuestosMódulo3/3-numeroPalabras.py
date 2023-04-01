"""
3. Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene. 
El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.
"""
cadena = input("Introduzca una cadena de caracteres: ")
palabras = 0
i = 0
while i < len(cadena):
    if cadena[i] == " " or i == len(cadena)-1:
        palabras += 1
    i += 1
print(f"El número de palabras de la cadena es {palabras}")