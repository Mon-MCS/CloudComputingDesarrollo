cadena = input("Introduzca una cadena: ")
anagrama = input("Introduzca el anagrama de la cadena: ")
if sorted(cadena) == sorted(anagrama):
    print(f"{anagrama} es anagrama de {cadena}")
else:
    print(f"{anagrama} no es anagrama de {cadena}")