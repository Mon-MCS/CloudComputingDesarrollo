import json

def clasificarGenero(lista):
    hombres = lista.count("H")
    mujeres = lista.count("M")
    hombresPorcentaje = round(hombres/len(lista),2)*100
    mujeresPorcentaje = round(mujeres/len(lista),2)*100
    return hombres, mujeres, hombresPorcentaje, mujeresPorcentaje


def mostrarEstadisticas():
    fichero = None
    try:
        file = input("Entre el nombre del fichero: ")
        fichero=open(file,"rt",encoding='UTF-8')
        contenido = fichero.read()
        h, m, porcentajeH, porcentajeM = clasificarGenero(list(contenido))
        print(f"En el archivo {file}: \nEl número de hombres es {h}.\nEl número de mujeres es {m}.\nEl porcentaje de hombres es {porcentajeH}%.\nEl porcentaje de mujeres es {porcentajeH}%.")
        guardar = input("¿Desea guardar estos resultados en un archivo JSON (s/n)? ")
        if guardar == "s":
            fileJSON = input("Entre el nombre del fichero con extensión JSON: ")
            ficheroJSON=open(fileJSON,"wt",encoding='UTF-8')
             
            info = {"Número hombres":h,
                    "Número mujeres":m,
                    "Porcentaje hombres":porcentajeH,
                    "Porcentaje mujeres":porcentajeM,
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