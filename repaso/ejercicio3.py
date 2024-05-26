"""
Tuplas:
Crea una tupla con tres elementos de diferentes tipos de datos.
Debes imprimir un mensaje accediendo y utilizando el segundo elemento de la tupla
Desempaqueta los elemento de la tupla guardando cada uno en variables separadas.
"""

tupla = ('Florencia', 37, True) #se pueden definir sin parentesis tambien

print(f'Mi edad es {tupla[1]}')

nombre, edad, soltera = tupla

print(nombre)
print(edad)
print(soltera)