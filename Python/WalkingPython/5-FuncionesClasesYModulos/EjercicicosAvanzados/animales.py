class SerVivo:
    def __init__(self, nombre):
        self.nombre = nombre
    def celulas(self):
        return True
class Animal(SerVivo):
    def __init__(self,alas):
        self.alas = alas
        super().__init__("Animal")
    def cuerdasVocales(self):
        return True

class Mamifero(Animal):
    def __init__(self, tipo_de_pelo="", habitat="", tipo_de_alimentacion="", tiempo_gestacion="", originario_d="", altura ="", peso=""):
        self.tipo_de_pelo = tipo_de_pelo
        self.habitat = habitat
        self.tipo_de_alimentacion = tipo_de_alimentacion
        self.tiempo_gestacion = tiempo_gestacion
        self.originario_d = originario_d
        self.altura = altura
        self.peso = peso
        super().__init__("No")
    def correr(self):
        return f"{self.nombre} corriendo"
    def saltar(self):
        return f"{self.nombre} volando"
    def nadar(self):
        return f"{self.nombre} nadando"
    def __reproducirse(self):
        return f"{self.nombre} reproduciéndose"
    

class Ave(Animal):
    def __init__(self, envergadura_de_alas="", tipo_de_plumaje="", habitat="", originario_de="", peso="", altura=""):
        self.envergadura_de_alas = envergadura_de_alas
        self.tipo_de_plumaje = tipo_de_plumaje
        self.habitat = habitat
        self.originario_de = originario_de
        self.peso = peso
        self.altura =altura
        super().__init__("Si")
    def volar(self):
        return f"{self.nombre} volando"
    def anidar(self):
        return f"{self.nombre} anidando"
    def __reproducirse(self):
        return f"{self.nombre} reproduciéndose"

humano = Mamifero("fino", "ciudad", "omnívoros", 9, "España", 1, 40)
print(humano.nombre)
print(humano.alas)
print(humano.tipo_de_alimentacion)
print(humano.correr())

        