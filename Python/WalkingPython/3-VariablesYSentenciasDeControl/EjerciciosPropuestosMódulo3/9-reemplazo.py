"""
9. Crea un programa en Python donde la entrada sean una cadena de caracteres, una palabra y una palabra de reemplazo,
el resultado debe ser la cadena con todas las ocurrencias de la palabra reemplazadas por otra palabra.
El programa debe utilizar un bucle `while` para buscar todas las ocurrencias de la palabra y reemplazarlas.
"""
cadena = input("Inserte una cadena: ")
palabra = input("Inserte la palabra a reemplazar: ")
reemplazo = input("Inserte la palabra a reemplazar: ")
i = 0
while i < len(cadena):
    if cadena[i:i+len(palabra)] == palabra:
        cadena = cadena[:i] + reemplazo + cadena[i+len(palabra):]
    i += 1
print(f"El resultado de reemplazar {palabra} por {reemplazo} en la cadena inial, ha sido {cadena}")