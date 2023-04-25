import json

def clasificarEdad(contenido):
    lista = json.loads(contenido.replace("'", '"'))
    mayoresDeEdad = 0
    for i in lista:
        if i>=18:
            mayoresDeEdad += 1
    mayoresDeEdad = 0
    for i in lista:
        if i>=18:
            mayoresDeEdad += 1
    menorEdad = min(lista)
    mayorEdad = max(lista)
    diccionarioEdades = {}
    for i in lista:
        if i not in diccionarioEdades:
            diccionarioEdades[i] = 1
        else:
            diccionarioEdades[i] += 1
    print(lista)
    for edad, cantidad in diccionarioEdades.items():
        print(f"El porcentaje de personas con {edad} años viene dado por el {round(cantidad/len(lista)*100,2)}%")
    return mayoresDeEdad, menorEdad, mayorEdad, diccionarioEdades

def mostrarEstadisticas():
    fichero = None
    try:
        file = input("Entre el nombre del fichero: ")
        fichero=open(file,"rt",encoding='UTF-8')
        contenido = fichero.read()
        mayoresDeEdad, menor, mayor, diccEdades= clasificarEdad(contenido)
        print(f"En el archivo {file}: \nEl número de personas mayores de edad es {mayoresDeEdad}.\nLa persona de menor edad tiene {menor} años.\nLa persona de mayor edad tiene {mayor} años.\nEl diccionario de las edades es {diccEdades}.")
        guardar = input("¿Desea guardar estos resultados en un archivo JSON (s/n)? ")
        if guardar == "s":
            fileJSON = input("Entre el nombre del fichero con extensión JSON: ")
            ficheroJSON=open(fileJSON,"wt",encoding='UTF-8')
             
            info = {"Personas mayores de edad":mayoresDeEdad,
                    "Persona de menor edad":menor,
                    "Persona de mayor edad":mayor,
                    "Diccionario de edades":diccEdades,
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