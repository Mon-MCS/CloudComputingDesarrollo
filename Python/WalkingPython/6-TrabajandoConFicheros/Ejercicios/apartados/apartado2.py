import json 
from random import randint

def fichero_exite(nombre_fichero):
    try:
        open(nombre_fichero)
    except Exception:
        return False
    return True

def ficheroLeerEscribir(contenido):
    fichero = None
    try:
        file = input("Entre el nombre del fichero: ")
        if (not fichero_exite(file)):
            print(f"El fichero {file} no existe, por lo que se crea a continuación")
            fichero=open(file,"wt",encoding='UTF-8')
            fichero.write(contenido)
            print("Escrito contenido en fichero")
        else:
            fichero=open(file,"rt",encoding='UTF-8')
            if file.endswith(".json"):
                contenidoJSON = fichero.read()
                contenido = json.loads(str(contenidoJSON))
                print(f"Leido contenido:\n {contenido}")
            else:
                contenido = fichero.read()
                print(f"Leido contenido:\n {contenido}")
    except Exception as e:
        print(f"E:{e}")
    finally:
        if fichero != None:
            fichero.close()
            print("Fichero cerrado")
if __name__ == "__main__":
    contenido = input("Introduzca el contenido del fichero en caso de que este no exista: ")
    ficheroLeerEscribir(contenido)