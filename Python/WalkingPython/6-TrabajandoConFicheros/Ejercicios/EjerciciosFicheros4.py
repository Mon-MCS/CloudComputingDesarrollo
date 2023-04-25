from random import randint, sample
import os
import time
from apartados.apartado1 import generarFichero
from apartados.apartado2 import ficheroLeerEscribir
from apartados.Ejercicio4apartado3 import mostrarEstadisticas

personas = []
for _ in range(100):
    genero = "F" if randint(0, 1) == 0 else "M"
    edad = randint(0, 120)
    persona = {"genero": genero, "edad": edad}
    personas.append(persona)
    


def ejercicio4():    
    while True:
        os.system("cls")
        print("1-Generar una lista aleatoria con temperaturas de las ciudades")
        print("2-Recuperar el diccionario del fichero en disco (si existe) o generar un nuevo diccionario")
        print("3-Mostrar con el diccionario generado o recuperado del disco las siguientes opciones estadísticas:")
        print(" 3.1- Encontrar la(s) ciudad(es) con la temperatura media anual más baja.")
        print(" 3.2- Encontrar la(s) ciudad(es) con la temperatura media anual más alta.")
        print(" 3.3- Ordenar las ciudades en orden descendente de temperatura media anual.")
        print("4-Salir")
        opcion = input("Seleccione una de las opciones mostradas: ")
        if int(opcion) == 1:
            NombreCiudades={"Madrid","Barcelona","Sevilla","Malaga","Cordoba","Toledo","Valencia","Bilbao","Salamanca","Palma","Caceres","Segovia","Saragoça ","Cuenca","Alicante","Las Palmas","Avila","Merida","Granada","Murcia"}
            # ciudades= dict()
            # for i in NombreCiudades:
            #     media_temperaturas=0 
            #     for j in range (0,12):
            #         media_temperaturas+=randint(-10,40)
            #     ciudades[i]=round(media_temperaturas/12,2)
            contenido = {i:round(sum(sample(range(-10,40),12))/12,2) for i in NombreCiudades}
            generarFichero(str(contenido))
            time.sleep(5)
        elif int(opcion) == 2:
            contenido = {i:round(sum(sample(range(-10,40),12))/12,2) for i in NombreCiudades}
            ficheroLeerEscribir(str(contenido))
            time.sleep(7)
        elif int(opcion) == 3:
            mostrarEstadisticas()
            time.sleep(10)
        elif int(opcion) == 4:
            print("Ha cerrado el ejercicio 4, hasta la próxima")
            time.sleep(3)
            break      
        else:
            print("Ha introducido una opción incorrecta")
if __name__ == "__main__":
    ejercicio4()