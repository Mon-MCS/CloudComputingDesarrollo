import random
numeroAleatorio = random.randint(1, 100)
numero = 0
while numeroAleatorio != numero:
    numero = int(input(f"Intente adivinar el número generado aleatoriamente entre 1 y 100, introduciendo un número: "))
    if numero > numeroAleatorio:
        print("El número introducido es mayor que el número aleatorio")
    elif numero < numeroAleatorio:
        print("El número introducido es menor que el número aleatorio")
    else:
        print("¡Enhorabuena ha acertado el número aleatorio!")