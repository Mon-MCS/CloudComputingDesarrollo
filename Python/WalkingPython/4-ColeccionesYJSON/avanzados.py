# 1. Crear una lista que contenga los números del 1 al 20, pero reemplazando 
# los múltiplos de 3 por `"EOI"`, los múltiplos de 5 por `"Cloud"` y los múltiplos de ambos por `"EOICloud"`.
lista = []
for i in range(1,21):
    if i%3 == 0 and i%5 == 0:
        lista.append("EOICloud")
    elif i%3 == 0:
        lista.append("EOI")
    elif i%5 == 0:
        lista.append("Cloud")
    else:
        lista.append(i)
print(lista)

# Para hacer compresión de listas con varias condiciones: <expr_1> if <condición_1> else <expr_2> if <condición_2> ... else <expr_n>
lista1 = ["EOICloud" if i%3 == 0 and i%5 == 0 else "EOI" if i%3 == 0 else "Cloud" if i%5 == 0 else i for i in range(1,21)]
print(lista1)

# 2. Crear un diccionario que contenga las palabras en una lista y la cantidad de veces que aparecen en ella.

#lista=input("Introduzca una sentencia: ").split()
# diccionario = {}
# for i in lista:
#     if i in diccionario.keys():
#         diccionario[i] += 1
#     else:
#         diccionario[i]=1
# print(diccionario)

diccionario= {}
for i in lista:
    if i not in diccionario:
        diccionario[i]=lista.count(i)
print(diccionario)

diccionario1 = {i:lista.count(i) for i in lista}
print(diccionario1)

# 3. Dado un texto con una lista de ciudades con su emblema mas importante, pedir las ciudades 
# para que las entre el usuario por teclado y crear un diccionario con su ciudad y su emblema. 
# **Nota** el diccionario deberá ordenarse por su clave.

# Lista de las ciudades con su emblema
listaTuplas = [("Nueva York", "La Estatua de la Libertad"),
                ("Tokio", "La flor del cerezo"),
                ("Paris", "La Torre Eiffel"),
                ("Londres", "El Big Ben"),
                ("Sídney", "La Opera de Sídney"),
                ("Buenos Aires", "El Obelisco"),
                ("Johannesburgo","El león"),
                ("Moscú", "El Kremlin"),
                ("Ámsterdam", "Los molinos de viento"),
                ("Dubai", "El Burj Khalifa")]

# Ciudades por teclado
n = int(input("Introduzca el número de ciudades del diccionario: "))
ciudad = []
for i in range(0,n):
    ciudad.append(input(f"Introduzca el nombre {i+1} de la ciudad: "))

# Bucle
dicOrdenado = {}
for i in sorted(ciudad):
    for j in range(0,len(listaTuplas)):
        if i == listaTuplas[j][0]:
            dicOrdenado[i] = listaTuplas[j][1]
print(dicOrdenado)

# Compresión
dicOrdenado1 = {i:listaTuplas[j][1] for i in sorted(ciudad) for j in range(0,len(listaTuplas)) if i == listaTuplas[j][0]}
print(dicOrdenado1)

# Parecido otro modo
ciudadesOrdenadas={ 
    "Ámsterdam": "Los molinos de viento",
    "Buenos Aires": "El Obelisco",
    "Johannesburgo": "El león",
    "Londres": "El Big Ben",
    "Moscú": "El Kremlin",
    "Nueva York": "La Estatua de la Libertad",
    "París": "La Torre Eiffel",
    "Sídney": "La Opera de Sídney",
    "Tokio": "La flor del cerezo",
    "Dubai": "El Burj Khalifa"
}
#while True:
#    ciudad=input("Ciudad:")
#    emblema=input("Emblema")
#    ciudadesOrdenadas[ciudad]=emblema
filtro=input("Por que desea filtrar el emblema")
ciudadConFiltro = {}
for ciudad,emblema in ciudadesOrdenadas.items():
    if emblema.startswith(filtro):
        ciudadConFiltro[ciudad]=emblema

ciudadConFiltro1 = {ciudad:emblema  for ciudad,emblema in ciudadesOrdenadas.items() if emblema.startswith(filtro)}
print(f"Ciudades cuyo emblema empieza con {filtro} son:")
print(ciudadConFiltro)
print(ciudadConFiltro1)