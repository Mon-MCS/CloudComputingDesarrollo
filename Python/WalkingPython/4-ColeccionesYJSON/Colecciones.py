def diccionario():
    frutas={"Manzanas":5,"Naranja":3,"Bananas":7}
    frutas["Peras"]=4
    print(frutas)
    del frutas["Naranja"]
    print(frutas)

    for fruta,cantidad in frutas.items():
        print(f"Tengo: {fruta} {cantidad}")

#Lista
def borradoDeElementosListas():
    lista=[1,6,3,4,5]
    print(lista)
    longitudLista = len(lista)
    i=0
    while(i<longitudLista):
        del lista[0]
        if i==3 or len(lista)<3:
            break
        i+=1
    print(lista)
    lista=[1,6,3,4,5]
    for i in range(len(lista)):
        del lista[0]
        if i==3 or len(lista)<3:
            break
    print(lista)


#Trabajo con Tuplas
def trabajoTuplas():
    #1 - Unir dos tuplas
    tuplaUno = (1,3,4)
    tuplaDos = (5,7,88)
    tuplaTres = tuplaUno+tuplaDos
    print(tuplaTres)
    #2 - Contar cuantas veces existe un elemento en la tupa
    tuplaCuatro=(1,23,3,1,3,1,34,1)
    print(tuplaCuatro)
    print(len(tuplaCuatro))
    print(tuplaCuatro.count(3))
    #3 - Encontrar el elemento que aparezca dado su indice
    print(tuplaCuatro.index(5)) # El 3 esta en la posición 2

#Conjuntos
conjunto = {1,2,3}
conjuntoUno = set()
conjunto.add(34)
conjuntoUno.add(1)
print(conjunto)
print(conjuntoUno)
#unir conjuntos
conjuntoTres = conjunto.union(conjuntoUno)
conjunto.remove(2)
print(conjunto)
#intersección de conjuntos
conjuntoCinco = {1,2,3}
conjuntoSeis = {3,4,5}
conjuntoSiete = conjuntoCinco.intersection(conjuntoSeis)
print(conjuntoSiete)
#subconjunto
conjuntoOcho = {1,2,3}
conjuntoNueve = {1,2}
print(conjuntoNueve.issubset(conjuntoOcho))
