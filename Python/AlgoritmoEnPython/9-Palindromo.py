cadena = input("Introduzca una cadena de texto: ")
cadenaInversa = ""
for i in range(len(cadena)-1,-1,-1):
    cadenaInversa += cadena[i]
if cadena == cadenaInversa:
    resultado = f"La cadena '{cadena}' es palíndromo"
else:
    resultado = f"La cadena '{cadena}' no es palíndromo"
print(resultado)