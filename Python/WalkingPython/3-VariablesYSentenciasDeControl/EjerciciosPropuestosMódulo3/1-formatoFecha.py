"""
1. Crea un programa en Python que acepte una fecha como cadena de caracteres en formato `"dd/mm/aaaa"` 
y devuelva la fecha en formato `"aaaa-mm-dd"`, con el año primero. 
El programa debe manejar excepciones en caso de que la cadena no tenga el formato correcto.
"""
from datetime import datetime
fecha = input("Introduzca una fecha cadena en formato dd/mm/aaaa: ")
try:
    obj = datetime.strptime(fecha,'%d/%m/%Y')
    print(f"{obj.year}-{obj.month}-{obj.day}")
except Exception as e:
    print(f"Se ha producido el error: \n{e}")