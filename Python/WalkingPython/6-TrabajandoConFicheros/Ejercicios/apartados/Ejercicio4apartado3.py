import json

def clasificarEdadyGenero(contenido):
    diccionario = json.loads(contenido.replace("'", '"'))
    # ciudadesTemperaturaMenor = []
    # for ciudad in diccionario.keys():
    #     if diccionario[ciudad] == min(diccionario.values()):
    #        ciudadesTemperaturaMenor.append(ciudad)
    ciudadesTemperaturaMenor = [ciudad for ciudad in diccionario.keys() if diccionario[ciudad] == min(diccionario.values())]
    ciudadesTemperaturaMayor= [ciudad for ciudad in diccionario.keys() if diccionario[ciudad] == max(diccionario.values())]
    # diccionarioOrdenado = {}
    # for temperatura in sorted(diccionario.values(), reverse=True):
    #         for ciudad in diccionario.keys():
    #             if diccionario[ciudad] == temperatura:
    #                 diccionarioOrdenado[ciudad]=temperatura
    diccionarioOrdenado = {ciudad:temperatura for temperatura in sorted(diccionario.values(), reverse=True) for ciudad in diccionario.keys() if diccionario[ciudad] == temperatura}
    print(diccionarioOrdenado)
    return ciudadesTemperaturaMenor, ciudadesTemperaturaMayor, diccionarioOrdenado
        
def mostrarEstadisticas():
    fichero = None
    try:
        file = input("Entre el nombre del fichero: ")
        fichero=open(file,"rt",encoding='UTF-8')
        contenido = fichero.read()
        ciudadesTempMenor, ciudadesTempMayor, diccOrdenado = clasificarEdadyGenero(contenido)
        print(f"En el archivo {file}:")
        if len(ciudadesTempMenor) >= 2:
            print(f"Las ciudades con la menor temperatura media anual de {min(diccOrdenado.values())} ºC son:")
            for i in ciudadesTempMenor:
                print(i)
        else:
            print(f"Las ciudad con la menor temperatura media anual de {min(diccOrdenado.values())} ºC es: {ciudadesTempMenor[0]}")
        
        if len(ciudadesTempMayor) >= 2:
            print(f"Las ciudades con la mayor temperatura media anual de {max(diccOrdenado.values())} ºC son:")
            for i in ciudadesTempMayor:
                print(i)
        else:
            print(f"Las ciudad con la mayor temperatura media anual de {max(diccOrdenado.values())} ºC es: {ciudadesTempMayor[0]}")
        print(f"Además las ciudades ordenadas en temperatura media anual descendente vienen dadas por: \n {diccOrdenado} ")
        guardar = input("¿Desea guardar estos resultados en un archivo JSON (s/n)? ")
        if guardar == "s":
            fileJSON = input("Entre el nombre del fichero con extensión JSON: ")
            ficheroJSON=open(fileJSON,"wt",encoding='UTF-8')
             
            info = {"Ciudad(es) con la temperatura media anual más baja":ciudadesTempMenor,
                    "ciudad(es) con la temperatura media anual más alta":ciudadesTempMayor,
                    "ciudades en orden descendente de temperatura media anual":diccOrdenado
                }
                
            infoJSON = json.dumps(info)
            print("Escrito contenido en fichero")
            ficheroJSON.write(infoJSON)
            ficheroJSON.close()
            print("Fichero JSON cerrado")
    except Exception as e:
        print(f"E:{e}")
    finally:
        if fichero != None:
            fichero.close()
            print("Fichero cerrado") 
if __name__ == "__main__":
    mostrarEstadisticas()