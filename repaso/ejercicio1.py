"""
Manipulación de cadenas: 
Crea un programa donde en una variable tipo string guardes tu nombre completo.
Luego debes lograr dividir el nombre y el apellido utilizando el método split() guardando cada dato en nuevas variables
Finalmente con el metodo print() y la interpolacion de cadenas (f string) debes imprimir un texto que incluya
el nombre que obtuviste usando el método split()
"""
input_name = input('Ingresa tu nombre y apellido: ')
total_name = list(input_name.split())
name = total_name[0]
last_name = total_name[1]

print(f'Tu nombre completo es: {name} {last_name}')

"""optimizado"""

input_name2 = input('Ingresa tu nombre y apellido: ')
name2, last_name2 = input_name2.split()
print(f'Tu nombre completo es: {name2} {last_name2}')
