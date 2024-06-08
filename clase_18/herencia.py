"""
ejercicio 1
- Crea la clase animal con atributos como especie, habitat, locomocion. La case debe tener el metodo comunicarse
- Luego crea clases hijas, ejemplo la clase perro que ladre, la clase gallina que cacaree
"""

class Animal:
    def __init__(self, especie, habitat, locomocion):
        self.especie = especie
        self.habitat = habitat
        self.locomocion = locomocion
        
    def comunicarse(self, sonido):
        print(f'La forma de comunicarse de un {self.especie} es a traves del {sonido}')
        
class Perro(Animal):
    def __init__(self, especie, habitat, locomocion, color):
        super().__init__(especie, habitat, locomocion)
        self.color = color
        
class Gallina(Animal):
    def __init__(self, especie, habitat, locomocion, color):
        super().__init__(especie, habitat, locomocion)
        self.color = color
        
perro1 = Perro('labrador', 'domestico', 'terrestre', 'marron')

perro1.comunicarse('ladrido')

gallina1 = Gallina('turuleca', 'campestre', 'terrestre', 'roja')

gallina1.comunicarse('cacareo')

"""
ejercicio 2
- Crea la clase vehiculo que tenga dos atributos, marca y modelo. la clase debe tener el metodo encender motor
- Luego crea clases hijas, como auto, motocicleta y camioneta
"""

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def encender_motor(self):
            print(f'Encendiendo el motor de tu {self.marca} {self.modelo}')

            
class Auto(Vehiculo):
    def __init__(self, marca, modelo, color, cant_puertas):
        super().__init__(marca, modelo)
        self.color = color
        self.cant_puertas = cant_puertas
        
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color
        
class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, color, capacidad):
        super().__init__(marca, modelo)
        self.color = color
        self.capacidad = capacidad
        
auto1 = Auto('Ford', 'Fiesta', 'Azul', 4)

auto1.encender_motor()

motocicleta1 = Motocicleta('Yamaha', 'XR', 'Roja')

motocicleta1.encender_motor()

camioneta1 = Camioneta('Jeep', '2007', 'Gris', '4 personas')

camioneta1.encender_motor()

"""
ejercicio 2
- Crea la clase libro con los atributos genero y numero de paginas, debe tener un metodo que indique en que pagina se encuentra
el lector y que porcentaje le falta por leer
- Luego crea clases hijas, como Rayuela de genero novela, con 470 paginas escrita por Julio Cortazar
"""

class Libro:
    def __init__(self, genero, num_paginas):
        self.genero = genero
        self.num_paginas = num_paginas
        
    def cuanto_falta(self, pag_actual):
        porcentaje = round(pag_actual * 100 / self.num_paginas)
        
        print(f'Tu libro tiene {self.num_paginas} y llevas leído un {porcentaje}% del libro')
        
class Novela(Libro):
    def __init__(self, genero, num_paginas, autor, nombre_libro):
        super().__init__(genero, num_paginas)
        self.autor = autor
        self.nombre_libro = nombre_libro
        
novela1 = Novela('Drama', 470, 'Julio Cortazar', 'Rayuela')

novela1.cuanto_falta(100)