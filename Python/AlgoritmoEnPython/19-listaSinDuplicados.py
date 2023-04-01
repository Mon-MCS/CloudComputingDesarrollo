n = int(input("Introduzca el número de enteros de la lista: "))
lista = []
listaNoDuplicados = []
for i in range(n):
    lista.append((int(input(f"Introduzca el entero de la posición {i}: "))))
for i in range(n):
    noEstaEnLista = True
    for j in range(len(listaNoDuplicados)):
        if lista[i] == listaNoDuplicados[j]:
            noEstaEnLista = False
            break
    if noEstaEnLista == True:
        listaNoDuplicados.append(lista[i])
print(f"La lista sin duplicados de la lista {lista} es {listaNoDuplicados}")