cadena = input("Introduzca una cadena: ")
anagrama = input("Introduzca el anagrama de la cadena: ")
if sorted(cadena) == sorted(anagrama):
    resultado = f"{anagrama} es anagrama de {cadena}"
else:
    resultado = f"{anagrama} no es anagrama de {cadena}"
print(resultado)