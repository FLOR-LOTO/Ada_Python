"""
Listas y enteros:
Crea un programa donde definas una variable tipo lista.
Los elementos de la lista seran 10 números entero aleatorios y de forma desordenada.
Debes agregar un numero mas al final utilizando el método append()
Luego debes tomar el primer y último numero de la lista y realizar alguna operación (suma, resta, multiplicacion, división)
por último debes lograr ordenar la lista de forma descendente con el método sorted()
"""

number_list = [10, 8, 5, 19, 12, 18, 20, 25, 30, 1]
number_list.append(14)
suma = number_list[0] + number_list[-1]
print(sorted(number_list, reverse=True))

#otra forma 

number_list.sort(reverse=True)
print(number_list)
