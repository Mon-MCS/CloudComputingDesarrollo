DNI = input("Introduzca los números del DNI: ")

def verificacion_DNI(dni):
    if len(dni) == 8:
        try:
            dni = int(dni)
            
        except Exception as e:
            print(f"Se ha producido el error: \n{e} \nPorque el DNI introducido es inválido")
            
        else:
            tablaLetrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
            resultadoResto = dni % 23 
            letra = tablaLetrasDNI[resultadoResto]  
            return print(f"La letra asociada al número de DNI {dni} es {letra}")
    else:
        return print("El DNI introducido es inválido")

verificacion_DNI(DNI)
        
            