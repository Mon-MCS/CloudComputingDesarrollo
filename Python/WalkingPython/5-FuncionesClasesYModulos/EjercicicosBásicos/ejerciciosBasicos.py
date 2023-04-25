'''
1. Crear una clase `Lapiz` que tenga los atributos `color` (cadena de caracteres) 
y `grosor` (entero). El constructor debe inicializar ambos atributos con valores 
por defecto. Agregar un método `escribir` que imprima por pantalla la frase 
"Escribiendo con un lapiz de [color] y grosor [grosor]". 
Crear un objeto de la clase `Lapiz` e invocar el método `escribir`.
'''

class Lapiz:
    def __init__(self,color="",grosor=""):
        self.color = color
        self.grosor = grosor
    def escribir(self):
        print(f"Escribiendo con un lápiz de {self.color} y grosor {self.grosor}")

miLapiz = Lapiz()
miLapiz.escribir()
miLapiz1 = Lapiz("azul","2B")
miLapiz1.escribir()

'''
2. Crear una clase `Flor` que tenga los atributos `nombre` (cadena de caracteres) 
y `color` (cadena de caracteres). El constructor debe recibir ambos atributos como 
argumentos e inicializarlos. Agregar un método `mostrar_informacion` que imprima 
por pantalla el nombre y color de la flor. Crear dos objetos de la clase `Flor`
e invocar el método `mostrar_informacion` para ambos.
'''

class Flor:
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
    def mostrar_informacion(self):
        print(f"El nombre de la flor es {self.nombre} y su color es {self.color}")

flor1 = Flor("rosa","roja")
flor2 = Flor("margarita", "blanca/amarilla")
flor1.mostrar_informacion()
flor2.mostrar_informacion()

'''
3. Dada la siguiente lista de productos. 
productos_lista = [
    {"nombre": "Leche", "precio": 2.50, "stock": 10},
    {"nombre": "Huevos", "precio": 1.50, "stock": 20},
    {"nombre": "Pan", "precio": 1.00, "stock": 15}
]

Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de productos.
'''
class Producto:
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def mostrar(self):
        print(f"nombre:{self.nombre}, precio:{self.precio}, stock:{self.stock}")
        
producto_lista = []
producto_lista.append(Producto("Leche", 2.50, 10))
producto_lista.append(Producto("Huevo", 1.50, 20))
producto_lista.append(Producto("Pan", 1.00, 15))
producto_lista[0].mostrar()
producto_lista[1].mostrar()
producto_lista[2].mostrar()

'''
4. Dada la siguiente lista de alumnos. 
alumnos_lista = [
       {"nombre": "Juan", "apellido": "Pérez", "edad": 20, "notas": [7, 8, 9]},
       {"nombre": "María", "apellido": "González", "edad": 22, "notas": [6, 9, 10]},
       {"nombre": "Pedro", "apellido": "García", "edad": 21, "notas": [5, 7, 8]} ]

Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de alumnos.

La clase deberá tener un método que incorpore el promedio de las notas del alumno.
'''
class Alumnos:
    def __init__(self,nombre, apellido, edad, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.notas = notas 
        self.media = ""
        
    def fmedia(self):
        try:
            self.media = round(sum(self.notas)/len(self.notas),2)
        except Exception as e:
            print(f"Se ha producido el siguiente error\n {e}")
    
    def mostrar(self):
        if self.media == "":
            print(f"El alumnos es {self.nombre} {self.apellido}, cuya edad es {self.edad} y sus notas son {self.notas}") 
        else:
            print(f"El alumnos es {self.nombre} {self.apellido}, cuya edad es {self.edad} y sus notas son {self.notas}, por lo que su nota media es {self.media}")        
alumnos_lista = []
alumnos_lista.append(Alumnos("Juan", "Pérez", 20, [7,8,9]))
alumnos_lista.append(Alumnos("María", "González", 22, [6,9,10]))
alumnos_lista.append(Alumnos("Pedro", "García", 21, [5,7,8]))
alumnos_lista[0].mostrar()
alumnos_lista[1].mostrar()
alumnos_lista[2].mostrar()

alumnos_lista[0].fmedia()
alumnos_lista[1].fmedia()
alumnos_lista[2].fmedia()

alumnos_lista[0].mostrar()
alumnos_lista[1].mostrar()
alumnos_lista[2].mostrar()

