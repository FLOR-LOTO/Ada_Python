"""
Crear una clase bicicleta:
- agregar el método init
- agregar al menos 3 atributos
- agregar al menos dos metodos
"""

class Bicicleta():
    
    def __init__ (self, color, material, tamaño):
        self.color = color
        self.material = material
        self.tamaño = tamaño
        print(f"Esta bicicleta es de color {self.color}, esta hecha de {self.material} y su tamaño es {self.tamaño}")
        
    def velocidad(self, tamaño):
        if tamaño == "grande":
          print(f'La bicicleta grande tiene una velocidad de 40 k/h')
        elif tamaño == "pequeña":
            print(f'La bicicleta pequeña tiene una velocidad de 20 k/h')
        else:
            print(f'La bicicleta mediana tiene una velocidad de 30 k/h')
            
    def altura(self, tamaño):
        if tamaño == "grande":
          print(f'La bicicleta grande mide 1.2 mtrs de alto')
        elif tamaño == "pequeña":
            print(f'La bicicleta pequeña mide 1 mtrs de alto')
        else:
            print(f'La bicicleta medidana mide 1.1 mtrs de alto')
            
bicicleta1 = Bicicleta("azul", "acero", "grande")

bicicleta1.velocidad("grande")

bicicleta1.altura("mediana")