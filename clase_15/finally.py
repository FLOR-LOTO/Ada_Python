"""finally permite ejecutar codigo a pesar del resultado del try/except"""

print('Inicio del programa...')

num1 = int(input('Ingrese un numero: '))

num2 = int(input('Ingrese un numero: ')) #si el usuario ingresa un cero nos daría error al divirlo

try:
    print(num1/num2)
except Exception as e: #guardo el error en la variable e
    print(f'No es posible dividir por {num2}')
    print(f'el ERROR: {e}')
finally:
    print('Programa finalizado')