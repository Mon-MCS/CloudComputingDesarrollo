# 1. Crear una lista que contenga las letras de una palabra, cada una en mayúscula
palabra = input("Introduzca una palabra: ")
# Bucle
lista = []
for i in palabra:
    lista.append(i.upper())
print(lista)
# Compresión
lista1 = [i.upper() for i in palabra]
print(lista1)

# 2. Crear un diccionario que contenga el cuadrado de cada número del 1 al 5
# Bucle
diccionario = {}
for i in range(1,6):
    diccionario[i]=i**2
print(diccionario)
# Compresión
diccionario1 = {i:i**2 for i in range(1,6)}
print(diccionario1)

# 3. Crear un diccionario que contenga los nombres y edades de varias personas
diccionarioNombre = {}
n = int(input("Introduzca el número de personas del diccionario: "))
nombre = []
edad = []
for i in range(0,n):
    nombre.append(input(f"Introduzca el nombre {i+1} del diccionario: "))
    edad.append(int(input(f"Introduzca la edad de {nombre}: ")))
    
for i in range(0,n):
    diccionarioNombre[nombre[i]] = edad[i]
print(diccionarioNombre)
diccionarioNombre1 = {nombre[i]:edad[i] for i in range(0,n)}
print(diccionarioNombre1)

# diccionario2 = (dict(zip(nombre, edad)))
# print(diccionario2)


