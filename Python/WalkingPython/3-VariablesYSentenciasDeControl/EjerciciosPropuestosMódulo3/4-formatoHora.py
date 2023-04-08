"""
4. Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y 
muestre la hora en 24 horas (por ejemplo, "7:30 PM" se convertiría en "19:30"). 
La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros.
"""
from datetime import datetime
formato = input("Introduzca una hora en formato 'hh:mm' PM/AM: ")
try:
    hora = datetime.strptime(formato,'%H:%M %p')
    if hora.hour <12:
        horaActualizada = datetime.strptime(formato,'%I:%M %p')
    else:
        horaActualizada = hora
    print(f"La hora {hora.hour}:{hora.minute} en formato 24 horas es {horaActualizada.hour}:{horaActualizada.minute}")
except Exception as e:
    print(f"Se ha producido el error: \n{e}")