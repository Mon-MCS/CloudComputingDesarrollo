"""
2. Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona. 
El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.
"""
from datetime import datetime
from pytz import timezone

zonaHoraria = input("Indique su zona horaria: ")
#print(pytz.all_timezones) permite ver todas las posibles zonas horarias
try: 
    print(datetime.now(timezone(zonaHoraria)))
except Exception as e:
    print(f"Se ha producido el error: \n{e}")