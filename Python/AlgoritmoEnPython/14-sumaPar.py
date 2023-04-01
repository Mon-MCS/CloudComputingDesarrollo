n = int(input("Introduzca el número de enteros de la lista: "))
lista = []
suma = 0
for i in range(n):
    lista.append((int(input(f"Introduzca el entero de la posición {i}: "))))
for i in lista:
    if i % 2 == 0:
        suma += i
print(f"La suma par de los elementos de la lista {lista} es {suma}")    
