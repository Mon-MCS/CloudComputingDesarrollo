from math import pi
class Figura:
    def __init__(self,nombre):
        self.nombre = nombre
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass
    def __str__(self):
        return self.nombre

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        super().__init__("Circulo")
    def calcular_area(self):
        return pi * self.radio ** 2
    def calcular_perimetro(self):
        return 2 * pi * self.radio

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
        super().__init__("Cuadrado")
    def calcular_area(self):
        return self.lado ** 2
    def calcular_perimetro(self):
        return 4 * self.lado

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        super().__init__("Triangulo")
    def calcular_area(self):
        return self.base * self.altura / 2
    def calcular_perimetro(self):
        return self.base + 2 * (self.altura ** 2 + self.base ** 2) ** 0.5