import json

def clasificarEdadyGenero(contenido):
    lista = json.loads(contenido.replace("'", '"'))
    mujeresMayoresEdad = 0
    for persona in lista:
        if persona["genero"] == "F" and persona["edad"] >= 18:
            mujeresMayoresEdad += 1
    hombresMenoresEdad = 0
    for persona in lista:
        if persona["genero"] == "M" and persona["edad"] < 18:
            hombresMenoresEdad += 1
    hombreMenorEdad = len(lista)
    for persona in lista:
        if persona["genero"] == "M":
            if persona["edad"] <= hombreMenorEdad:
                hombreMenorEdad = persona["edad"]
    mujerMenorEdad = len(lista)
    for persona in lista:
        if persona["genero"] == "F":
            if persona["edad"] <= mujerMenorEdad:
                mujerMenorEdad = persona["edad"]
    listaEdadesHombres = [persona["edad"] for persona in lista if persona["genero"]=="M"]
    promedioHombres = round(sum(listaEdadesHombres)/len(lista),2)
    listaEdadesMujeres = [persona["edad"] for persona in lista if persona["genero"]=="F"]
    promedioMujeres = round(sum(listaEdadesMujeres)/len(lista),2)
    return mujeresMayoresEdad, hombresMenoresEdad, hombreMenorEdad, mujerMenorEdad, promedioHombres, promedioMujeres
        

def mostrarEstadisticas():
    fichero = None
    try:
        file = input("Entre el nombre del fichero: ")
        fichero=open(file,"rt",encoding='UTF-8')
        contenido = fichero.read()
        ms, hs, h, m, ph, pm = clasificarEdadyGenero(contenido)
        print(f"En el archivo {file}: \nel número de mujeres mayores de edad es {ms}.\nEl número de hombres menores de edad es {hs}.\nLa edad menor entre los hombres es {h} años.\nla edad menor entre las mujeres es {m} años.\nEl promedio de edad de los hombres es {ph} años.\npromedio de edad de las mujeres es {pm} años.")
        guardar = input("¿Desea guardar estos resultados en un archivo JSON (s/n)? ")
        if guardar == "s":
            fileJSON = input("Entre el nombre del fichero con extensión JSON: ")
            ficheroJSON=open(fileJSON,"wt",encoding='UTF-8')
             
            info = {"Mujeres mayores de edad":ms,
                    "Hombres menores de edad":hs,
                    "Hombre de menor edad":h,
                    "Mujer de menor edad":m,
                    "Promedio edad de los hombre":ph,
                    "Promedio edad mujeres":pm
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