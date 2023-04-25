from random import randint
def generarFichero(contenido):
    file = input("Entre el nombre del fichero: ")
    fichero=open(file,"wt",encoding='UTF-8')
    fichero.write(contenido)
    print("Escrito contenido en fichero")
    fichero.close()
    print("Fichero cerrado")

if __name__ == "__main__":
    contenido = input("Introduzca el contenido del fichero: ")
    generarFichero(contenido)