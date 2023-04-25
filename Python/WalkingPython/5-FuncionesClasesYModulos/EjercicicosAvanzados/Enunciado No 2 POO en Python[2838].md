# POO en Python 

## Primera parte

#### Ejercicios de Programación Orientada a Objetos

A continuación encontrará dos escenarios para que implemente todos los pilares de la POO.

- Clases y Objetos
- Atributos y Métodos
- Herencia
- Abstracción
- Encapsulación
- Polimorfismo

Deberá crear los programas en Python, que demuestren cada uno de los pilares de la POO .

##### Escenario: Coches

En este escenario, se tienen las siguientes clases:

- `Vehiculo`: clase base que representa un vehículo genérico.
- `Coche`: clase derivada de `Vehiculo` que representa un coche en específico.
- `Camion`: clase derivada de `Vehiculo` que representa un camión en específico.
- `Motocicleta`: clase derivada de `Vehiculo` que representa una motocicleta en específico.

Cada clase derivada tiene sus propios atributos y métodos, específicos de cada tipo de vehículo. Por ejemplo, la clase `Coche` deberá tener los atributos `marca`, `modelo`, `año`, `kilometraje`, `fabricante`,`numero_de_bastidor`, `color`, `numero_puertas`, `tara`. `numero_de_ruedas` y métodos como `acelerar`, `frenar`, `encender_luces`, `armar_alarma`,`desarmar_alarma`,`repostar`. 

Deberá definir los atributos y métodos para `Camion` , `Motocicleta` y `Vehiculo` respectivamente.

##### Escenario: Animales

En este escenario, se tienen las siguientes clases:

- `SerVivo`: clase base que representa un ser vivo genérico.
- `Animal`: clase derivada de `SerVivo` que representa un animal en específico.
- `Mamifero`: clase derivada de `Animal` que representa un mamífero en específico.
- `Ave`: clase derivada de `Animal` que representa un ave en específico.

Cada clase derivada tiene sus propios atributos y métodos, específicos de cada tipo de animal. Por ejemplo, la clase `Mamifero` deberá tener atributos como `tipo_de_pelo`, `hábitat`, `tipo_de_alimentación`, `tiempo_gestacion`, `originario_d`, `altura `, `peso` y métodos como `correr`,`saltar`, `nadar` , `reproducirse`. La clase `Ave`, por otro lado, deberá tener atributos como `envergadura_de_alas`, `tipo_de_plumaje`, `hábitat`, `originario_de` , `peso` y `altura` y métodos como `volar`, `anidar`, `reproducirse`. 

Deberá definir los atributos y métodos para las clases `Animal` y `SerVivo` respectivamente.

___

## Segunda Parte

Basado en el popular vídeo juego `Resident Evil`. Tenemos la siguiente jerarquía de clases:

- Personaje
  - Enemigo
    - Zombie
    - Perro
    - Boss
  - Jugador
- Item
  - Arma
    - Pistola
    - Escopeta
  - Botiquin

Se ha generado las siguiente clases

```
class Personaje:
    def __init__(self, nombre, salud, ataque, defensa):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa

    def recibir_dano(self, dano):
        self.salud = max(0, self.salud - dano)

    def atacar(self, personaje):
        dano = max(0, self.ataque - personaje.defensa)
        personaje.recibir_dano(dano)
        return dano

    def morir(self):
        print(f'{self.nombre} ha muerto.')

class Enemigo(Personaje):
    def __init__(self, nombre, salud, ataque, defensa, recompensa):
        super().__init__(nombre, salud, ataque, defensa)
        self.recompensa = recompensa

    def atacar(self, personaje):
        dano = max(0, self.ataque - personaje.defensa)
        personaje.recibir_dano(dano)
        print(f'{self.nombre} atacó a {personaje.nombre} y le hizo {dano} de daño.')
        if personaje.salud == 0:
            personaje.morir()
            return self.recompensa

    def morir(self):
        print(f'{self.nombre} ha sido derrotado.')
        return self.recompensa

class Jugador(Personaje):
    def __init__(self, nombre, salud, ataque, defensa, inventario=[]):
        super().__init__(nombre, salud, ataque, defensa)
        self.inventario = inventario

    def usar_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
            item.usar(self)

class Zombie(Enemigo):
    def __init__(self, nombre='Zombie', salud=100, ataque=10, defensa=5, recompensa=10):
        super().__init__(nombre, salud, ataque, defensa, recompensa)

class Perro(Enemigo):
    def __init__(self, nombre='Perro', salud=80, ataque=20, defensa=10, recompensa=20):
        super().__init__(nombre, salud, ataque, defensa, recompensa)

class Boss(Enemigo):
    def __init__(self, nombre, salud, ataque, defensa, recompensa):
        super().__init__(nombre, salud, ataque, defensa, recompensa)

class Item:
    def __init__(self, nombre, efecto):
        self.nombre = nombre
        self.efecto = efecto

    def usar(self, personaje):
        pass

class Botiquin(Item):
    def __init__(self):
        super().__init__('Botiquin', 'restaura 20 puntos de salud')

    def usar(self, personaje):
        personaje.salud = min(personaje.salud + 20, 100)

class Arma(Item):
    def __init__(self, nombre, ataque):
        super().__init__(nombre, f'aumenta el ataque en {ataque} puntos')
        self.ataque = ataque

    def usar(self, personaje):
        personaje.ataque += self.ataque

class Pistola(Arma):
    def __init__(self):
        super().__init__('Pistola', 20)

class Escopeta(Arma):
    def __init__(self):
        super().__init__('Escopeta', 30)
```

# implementado el polimorfismo objetos de diferenets classes que responden diferente a la llamada del mismo metodo o funcion
def comportamiento(enemigo,jugador):
    enemigo.atacar(jugador)
    enemigo.morir()

if name == "main":

    jugador1 = Jugador("Billy",200,100,50)
    #Crear enemigos
    zombie1 = Zombie()
    perro1 = Perro()
    boos1 = Boss("jefe1",50,10,20,50)

    comportamiento(zombie1,jugador1)
    comportamiento(perro1,jugador1)
    comportamiento(boos1,jugador1)

Responda a las siguiente preguntas:

1. ¿Cuál es la clase base en este escenario?
    La clases bases son Personaje y Item.
2. ¿Qué métodos tienen todas las clases en común?
    Los métodos que tienen en común las clases derivadas de Personaje son recibir_daño, atacar y morir.
    Por otra parte, las clases derivadas de Item tiene el método usar.
3. ¿Qué método se debe implementar en cada clase derivada para recibir daño?
    El método recibir daño.
4. ¿Qué método se debe implementar en cada clase derivada para atacar a otro personaje?
    El método atacar.
5. ¿Cómo se usa la herencia en este escenario?
    La clases Jugador y Enemigo heredan de Personaje, a su vez Zombie, Perro y Boss heredan de Enemigo. Por otra parte, Arma y Botiquin heredan de Item y a su vez Pistora y Escopeta heredan de Arma.
6. ¿Cómo se usa el polimorfismo en este escenario?
    Pues en la clase enemigos se ha aplicado a atacar y morir y en las clases derivadas de ítems (Botiquín y Arma) se emplea en usar.
7. ¿Cómo se usa la encapsulación en este escenario?
    En este caso no se emplea el ancapsulamiento.
8. ¿Cómo se usa la abstracción en este escenario?
    Especificándose los atributos de cada clase.
