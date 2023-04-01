"""
8. Crea un programa en Python que acepte una lista de cadenas de caracteres y devuelva una nueva lista que contenga 
solo las cadenas que tienen más de 5 caracteres. 
El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.
"""
n = int(input("Introduzca el número de cadenas de la lista: "))
listaPalabras = []
lista5caracteres = []
for i in range(n):
    listaPalabras.append((input(f"Introduzca la cadena de la posición {i}: ")))
for i in range(n):
    if len(listaPalabras[i]) > 5:
        lista5caracteres.append(listaPalabras[i])
        
print(f"La lista con cadenas que tienen más de 5 caracteres de la lista {listaPalabras} es {lista5caracteres}")