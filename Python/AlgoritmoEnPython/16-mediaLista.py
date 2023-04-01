n = int(input("Introduzca el número de enteros de la lista: "))
lista = []
suma = 0
for i in range(n):
    lista.append((int(input(f"Introduzca el entero de la posición {i}: "))))
for i in range(n):
    suma += lista[i]
print(f"La suma de los elementos de la lista {lista} es {suma}")    
