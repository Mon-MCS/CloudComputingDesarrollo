## POO en Python

Dadas el siguiente programa de Python:

```
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
        super().__init__("Circulo")
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
```



Responder a las siguientes preguntas.

## Cuestionario

1. ¿Qué clase es la clase base en este programa?

   La clase Figura.

2. ¿Qué métodos tienen todas las clases en común?

  Los métodos de la clase base, esto es el constructor __str__ y los métodos calcular_area y calcular_perimetro.

3. ¿Qué método se debe implementar en cada clase derivada para calcular el área de la figura?

​	El método calcular_area de cada clase heredada.

4. ¿Qué método se debe implementar en cada clase derivada para calcular el perímetro de la figura?

   El método calcular_perimetro de cada clase heredada.

5. ¿Qué significa la palabra clave `super()` en el método `init` de las clases derivadas?

​	Significa que está recurriendo a la clase padre.

6. ¿Qué método se utiliza para imprimir el nombre de la figura?

​	Con el método __str__.

7. ¿Qué es la herencia en programación orientada a objetos (POO)? ¿Cómo se aplica en las clases `Circulo`, `Cuadrado` y `Triangulo` del programa?

    La herencia es la capacidad de una clase de obtener características de otra no tan específica. Todas heredan los métodos, atributos y propiedades de la clase base.

8. ¿Qué es el polimorfismo en POO? ¿Cómo se aplica en las clases `Circulo`, `Cuadrado` y `Triangulo` del programa?

    Es la capacidad de adoptar múltiples formas, con los mismos datos se han hayado las áreas y los parímetros de diferentes figuras.

    Otra forma: El polimorfismo en POO es la capacidad de los objetos de diferentes clases de responder al mismo mensaje de manera diferente. En el programa presentado, el polimorfismo se aplica en las clases Circulo, Cuadrado y Triangulo al tener cada una su propia implementación de los métodos calcular_area() y calcular_perimetro().

9. ¿Qué es la encapsulación en POO? ¿Cómo se aplica en las clases del programa presentado?

    Es la facultad de ocultar valores y no se está aplicando aquí en ningún caso.

10. ¿Qué es la abstracción en POO? ¿Cómo se aplica en las clases del programa presentado?

    Son las características especificas de un objeto, las que lo diferencian del resto. En este caso, cada figura tiene su propia forma de calcular su área y su perímetro.