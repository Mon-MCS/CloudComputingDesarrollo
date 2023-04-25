import os
from EjerciciosFicheros1 import ejercicio1
from EjerciciosFichero2 import ejercicio2
from EjerciciosFichero3 import ejercicio3
from EjerciciosFicheros4 import ejercicio4
while True:
        os.system("cls")
        print("Se encuentra en el menú principal de ejercicios con ficheros.")
        print("1-Lista de hombres y mujeres")
        print("2-Lista de personas por edades")
        print("3-Lista de Personas")
        print("4-Temperatura mensual de 20 ciudades")
        print("5-Salir")
        opcion = input("Seleccione una de las opciones mostradas: ")
        if int(opcion) == 1:
            ejercicio1()
        elif int(opcion) == 2:
            ejercicio2()
        elif int(opcion) == 3:
            ejercicio3()
        elif int(opcion) == 4:
            ejercicio4()
        elif int(opcion) == 5:
            print("Hasta la próxima")
            break      
        else:
            print("Ha introducido una opción incorrecta")