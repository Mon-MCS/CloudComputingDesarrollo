n = int(input("Introduzca el número de enteros de la lista: "))
listaPalabras = []

for i in range(n):
    listaPalabras.append((input(f"Introduzca la cadena de la posición {i}: ")))

print("La lista que ha introducido es:", listaPalabras)

listaOrdenada = sorted(listaPalabras)
print("La lista ordenada viene dada por: \n", listaOrdenada)