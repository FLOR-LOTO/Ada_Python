"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad, patente )
 *El atributo patente debe ser PRIVADO
-Métodos ( __init__() y __str__() )
 *Crear los métodos que me permitan mostrar y modificar el valor del
 atributo privado

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )


Instanciar un objeto de cada clase
"""

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return f'Vehiculo de color {self.color} con {self.ruedas} ruedas'
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, patente):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.__patente = patente
        
    def __str__(self):
      return f'Coche de color {self.color}, {self.ruedas} ruedas, velocidad {self.velocidad} km/h'
    
    @property
    def patente(self):
        return self.__patente
    
    @patente.setter
    def patente(self, nueva_patente):
        self.__patente = nueva_patente
        

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        

coche1 = Coche('rojo', 4, 200, 12345)

print(coche1)
print(coche1.patente)
coche1.patente = 6789
print(coche1.patente)

bici1 = Bicicleta('negro', 2, 'todo terreno')

print(bici1)