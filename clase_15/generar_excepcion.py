radio = int(input('ingrese un valor: '))

if radio < 0:
    raise Exception('el radio no puede ser menor a 0')