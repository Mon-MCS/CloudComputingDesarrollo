class Vehiculo:
    def __init__(self,tipo_vehiculo="", marca="", modelo="", año="", kilometraje="", fabricante="", numero_de_bastidor="", color="", numero_puertas="", tara=""):
        self.tipo_vehiculo = tipo_vehiculo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.fabricante = fabricante
        self.numero_de_bastidor = numero_de_bastidor
        self.color = color
        self.numero_puertas = numero_puertas
        self.tara = tara
    
class Coche(Vehiculo):
    ruedas = 4
    tipo_vehiculo = "Coche"
    def __init__(self, marca="", modelo="", año="", kilometraje="", fabricante="", numero_de_bastidor="", color="", numero_puertas="", tara=""):
        super().__init__(self,marca, modelo, año, kilometraje, fabricante, numero_de_bastidor, color, numero_puertas, tara)
    def acelerar(self):
        return f"Acelerando {Coche.tipo_vehiculo} modelo {self.marca}"
    def frenar(self):
        return f"{Coche.tipo_vehiculo} modelo {self.marca} frenando"
    def encender_luces(self):
        return f"{Coche.tipo_vehiculo} modelo {self.marca} encendiendo luces"
    def armar_alarma(self):
        return f"Alarmas del {Coche.tipo_vehiculo} modelo {self.marca} encendidas"
    def __desarmar_alarma(self):
        return f"Alarmas del {Coche.tipo_vehiculo} modelo {self.marca} apagadas"
    def repostar(self):
        return f"Se ha repostado el {Coche.tipo_vehiculo} modelo {self.marca}"
        
        
class Camion(Vehiculo):
    tipo_vehiculo = "Camión"
    def __init__(self, marca="", modelo="", año="", kilometraje="", fabricante="", numero_de_bastidor="", color="", numero_puertas="", tara="", numero_de_ruedas=""):
        super().__init__(self,marca, modelo, año, kilometraje, fabricante, numero_de_bastidor, color, numero_puertas, tara, numero_de_ruedas)
    def acelerar(self):
        return f"Acelerando {Camion.tipo_vehiculo} modelo {self.marca}"
    def frenar(self):
        return f"{Camion.tipo_vehiculo} modelo {self.marca} frenando"
    def encender_luces(self):
        return f"{Camion.tipo_vehiculo} modelo {self.marca} encendiendo luces"
    def armar_alarma(self):
        return f"Alarmas del {Camion.tipo_vehiculo} modelo {self.marca} encendidas"
    def __desarmar_alarma(self):
        return f"Alarmas del {Camion.tipo_vehiculo} modelo {self.marca} apagadas"
    def repostar(self):
        return f"Se ha repostado el {Camion.tipo_vehiculo} modelo {self.marca}"

class Motocicleta(Vehiculo):
    tipo_vehiculo = "Motocicleta"
    ruedas = 2
    puertas = 0
    def __init__(self, marca="", modelo="", año="", kilometraje="", fabricante="", numero_de_bastidor="", color="", tara=""):
        super().__init__(self,marca, modelo, año, kilometraje, fabricante, numero_de_bastidor, color, tara)
    def acelerar(self):
        return f"Acelerando {Motocicleta.tipo_vehiculo} modelo {self.marca}"
    def frenar(self):
        return f"{Motocicleta.tipo_vehiculo} modelo {self.marca} frenando"
    def encender_luces(self):
        return f"{Motocicleta.tipo_vehiculo} modelo {self.marca} encendiendo luces"
    def armar_alarma(self):
        return f"Alarmas de la {Motocicleta.tipo_vehiculo} modelo {self.marca} encendidas"
    def __desarmar_alarma(self):
        return f"Alarmas de la {Motocicleta.tipo_vehiculo} modelo {self.marca} apagadas"
    def repostar(self):
        return f"Se ha repostado la {Motocicleta.tipo_vehiculo} modelo {self.marca}"

coche = Coche("Lamborghini", "Sian", 2021, 0, "Lego", 232120, "verde", 3, 123)

print(coche.ruedas)
print(coche.marca)
print(coche.acelerar())    

moto= Motocicleta(marca="BMW")
print(Motocicleta.tipo_vehiculo)
print(moto.marca)
print(moto.repostar())
        
        
        