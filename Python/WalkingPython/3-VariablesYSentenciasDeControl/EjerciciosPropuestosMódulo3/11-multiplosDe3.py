"""
11. Crea un programa en Python que tome una lista de números enteros y devuelva una nueva lista
que contenga solo los números que son múltiplos de 3. 
El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar los números.
"""
n = int(input("Introduzca el número de enteros de la lista: "))
lista = []
listaMultiplos3 = []
for i in range(n):
    lista.append((int(input(f"Introduzca el entero de la posición {i}: "))))
for i in range(n):
    if lista[i] % 3 == 0:
        listaMultiplos3.append(lista[i])
print(f"La lista de los elementos múltiplos de 3 de la lista {lista} es {listaMultiplos3}")    