class Animal:
  especie = "mamifero"   # atributo

  def __init__(self, nombre, raza):  # método constructor -> caracteristicas para crear un objeto
    self.nombre = nombre
    self.raza = raza

  def mostrar(self, nombre_dueno):    #metodo
    print(f"nombre = {self.nombre} raza = {self.raza} su dueño es = {nombre_dueno}")
    
  def otro_metodo(self): #cuando pongo self, puedo acceder a todos los atributos y metodos que esten detro del constructor
      self.mostrar()
      self.nombre


perro1 = Animal("lola", "salchicha")

perro1.mostrar("Flor")


perro2 = Animal("peque", "bulldog")

perro2.mostrar("Flor")


list = {"a": 1, "b":2}

print(dir(list)) #inspeccionar un objeto, devuelve una lista con los atributos inclusive los heredados

print(vars(perro1)) #imprime los atributos de un objeto en un diccionario es equivalente al metodo __dict__