f = open("./datasets/txt_lectura.txt")

print(f.read())

f.close()

"""hace lo mismo pero de esta forma no hace falta que cerremos el archivo"""

with open("./datasets/txt_lectura.txt") as f:
    print(f.read())
    
"""Puedo pedir que me lea solo los primeros caracteres"""

with open("./datasets/txt_lectura.txt") as f:
    print(f.read(10))
    
"""Puedo pedir que me lea una cierta cantidad de lineas"""

with open("./datasets/txt_lectura.txt") as f:
    print(f.readline()) #lee la primera 
    print(f.readline()) #lee la primera y la segunda