from random import randint
import os
import time
from apartados.apartado1 import generarFichero
from apartados.apartado2 import ficheroLeerEscribir
from apartados.Ejercicio2apartado3 import mostrarEstadisticas
def ejercicio2():    
    while True:
        os.system("cls")
        print("1-Generar una lista aleatoria con datos de las edades de 100 personas")
        print("2-Recuperar la lista del fichero en disco (si existe) o generar una nueva lista")
        print("3-Mostrar con la lista generada o recuperada del disco las siguientes opciones estadísticas: \n 3.1- Número de hombres. \n 3.2- Número de mujeres.\n 3.3.-Porcentaje de hombres y mujeres.")
        print("4-Salir")
        opcion = input("Seleccione una de las opciones mostradas: ")
        if int(opcion) == 1:
            contenido = str([randint(0,125) for n in range(1,101)])
            generarFichero(contenido)
            time.sleep(5)
        elif int(opcion) == 2:
            contenido = str([randint(0,125) for n in range(1,101)])
            ficheroLeerEscribir(contenido)
            time.sleep(7)
        elif int(opcion) == 3:
            mostrarEstadisticas()
            time.sleep(10)
        elif int(opcion) == 4:
            print("Ha cerrado el ejercicio 2, hasta la próxima")
            time.sleep(3)
            break      
        else:
            print("Ha introducido una opción incorrecta")
if __name__ == "__main__":
    ejercicio2()