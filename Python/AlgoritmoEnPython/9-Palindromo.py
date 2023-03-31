cadena = input("Introduzca una cadena de texto: ")
cadenaInversa = ""
for i in range(len(cadena)-1,-1,-1):
    cadenaInversa += cadena[i]
if cadena == cadenaInversa:
    print(f"La cadena '{cadena}' es palíndromo")
else:
    print(f"La cadena '{cadena}' no es palíndromo")