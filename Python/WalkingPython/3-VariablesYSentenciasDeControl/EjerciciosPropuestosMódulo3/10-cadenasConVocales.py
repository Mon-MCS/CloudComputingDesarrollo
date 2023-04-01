"""
10. Crea un un programa en Python que tome una lista de cadenas de caracteres y devuelva 
una nueva lista que contenga solo las cadenas que contienen al menos una vocal.
La función debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.
"""
n = int(input("Introduzca el número de cadenas de la lista: "))
listaPalabras = []
listaConVocales = []
for i in range(n):
    listaPalabras.append((input(f"Introduzca la cadena de la posición {i}: ")))
for i in range(n):
    if "a" in listaPalabras[i] or "e" in listaPalabras[i] or "i" in listaPalabras[i] or "o" in listaPalabras[i] or "u" in listaPalabras[i]:
        listaConVocales.append(listaPalabras[i])
# Otro modo:
# vocales = ["a", "e", "i", "o", "u"]
# for i in range(n):
    #for i in vocales:
        #if i in listaPalabras[i]:
            #listaConVocales.append(listaPalabras[i])
            #break
print(f"La lista con cadenas que tienen más de 5 caracteres de la lista {listaPalabras} es {listaConVocales}")