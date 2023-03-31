from math import pi

numero = float(input("Introduzca el radio del círculo: "))

def areaPerimetro(radio):
    area = round(radio*pi*2,4)
    perimetro = round(pow(radio,2)*pi,4) 
    return area, perimetro

area , perimetro = areaPerimetro(numero)
print(f"El área del círculo es {area} y el perímetro el círculo es {perimetro}")