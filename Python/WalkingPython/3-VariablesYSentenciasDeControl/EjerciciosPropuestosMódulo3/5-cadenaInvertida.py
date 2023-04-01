"""
5. Crea un programa en Python que acepte una cadena de caracteres y devuelva la 
cadena invertida (por ejemplo, "hola" se convertiría en "aloh"). 
El programa debe utilizar un bucle `for` para recorrer la cadena y construir la cadena invertida.
"""
cadena = input("Introduzca una cadena de texto: ")
cadenaInversa = ""
for i in range(len(cadena)-1,-1,-1):
    cadenaInversa += cadena[i]
print(f"La cadena invertida de {cadena} es {cadenaInversa}")