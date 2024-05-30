#resultado NameError: name 'b' is not defined
# a = 2
# if b > 3:
#     print(b)

"""python nos permite controlar las excepciones usando: 
     try/except
"""
print('Inicio del programa...')

num1 = int(input('Ingrese un numero: '))

num2 = int(input('Ingrese un numero: ')) #si el usuario ingresa un cero nos daría error al divirlo

try:
    print(num1/num2)
except Exception as e: #guardo el error en la variable e
    print(f'No es posible dividir por {num2}')
    print(f'el ERROR: {e}')
    
print('Programa finalizado')

#el Exception es un error generico, pero tambien podemos especificar con que tipo de error queremos que haga la excepcion
# por ejemplo: 
# except division by zero:
#     print(f'No es posible dividir por {num2}')