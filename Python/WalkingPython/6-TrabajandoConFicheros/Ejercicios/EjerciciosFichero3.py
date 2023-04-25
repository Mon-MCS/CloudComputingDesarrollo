from random import randint
import os
import time
from apartados.apartado1 import generarFichero
from apartados.apartado2 import ficheroLeerEscribir
from apartados.Ejercicio3apartado3 import mostrarEstadisticas

personas = []
for _ in range(100):
    genero = "F" if randint(0, 1) == 0 else "M"
    edad = randint(0, 120)
    persona = {"genero": genero, "edad": edad}
    personas.append(persona)
    


def ejercicio3():    
    while True:
        os.system("cls")
        print("1-Generar una lista aleatoria con datos de las edades y generos de 100 personas")
        print("2-Recuperar la lista del fichero en disco (si existe) o generar una nueva lista")
        print("3-Mostrar con la lista generada o recuperada del disco las siguientes opciones estadísticas:")
        print(" 3.1- Contar el número de mujeres mayores de edad (con edad mayor o igual a 18).")
        print(" 3.2- Contar el número de hombres menores de edad (con edad menor a 18).")
        print(" 3.3- Encontrar la edad menor entre los hombres.")
        print(" 3.4- Encontrar la edad menor entre las mujeres.")
        print(" 3.5- Calcular el promedio de edad de los hombres.")
        print(" 3.6- Calcular el promedio de edad de las mujeres.")
        print("4-Salir")
        opcion = input("Seleccione una de las opciones mostradas: ")
        if int(opcion) == 1:
            contenido = []
            for _ in range(100):
                genero = "F" if randint(0, 1) == 0 else "M"
                edad = randint(0, 120)
                contenido.append({"genero": genero, "edad": edad})
            generarFichero(str(contenido))
            time.sleep(5)
        elif int(opcion) == 2:
            contenido = []
            for _ in range(100):
                genero = "F" if randint(0, 1) == 0 else "M"
                edad = randint(0, 120)
                contenido.append({"genero": genero, "edad": edad})
            ficheroLeerEscribir(str(contenido))
            time.sleep(7)
        elif int(opcion) == 3:
            mostrarEstadisticas()
            time.sleep(10)
        elif int(opcion) == 4:
            print("Ha cerrado el ejercicio 3, hasta la próxima")
            time.sleep(3)
            break      
        else:
            print("Ha introducido una opción incorrecta")
if __name__ == "__main__":
    ejercicio3()