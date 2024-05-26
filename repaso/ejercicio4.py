"""
Diccionarios:
Crea un diccionario con claves como nombre de paises y valores como sus capitales.
Lugo de haber definido el diccionario inicial debes agregar un nuevo par de clave-valor
Finalmente imprime un mensaje usando f-string accediendo a alguno de los valores del diccionario utilizando su clave
"""

diccionario = {
                'Argentina':'Buenos Aires',
                'Colombia':'Bogota',
                'Venezuela':'Caracas'
              }

diccionario.update({'chile':'Santiago de Chile'})

print(f'Florencia quiere viajar a: {diccionario["Colombia"]}')

print(diccionario['Argentina']) 