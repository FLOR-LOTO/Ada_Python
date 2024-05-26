# Una función principal llamada solicitud()
    # Mostrará un mensaje de bienvenida
    # Pedirá la cantidad de colectivos a cargar
    # Por cada colectivo se va a poder cargar los datos de los pasajeros
    # Llamar a otra función llamda carga_pasajero(), le tenemos que pasar la cantidad de pasajeros.

# Cargar los datos de cada pasajero para cada colectivo
    # Nombre
    # Edad
    # Esta función tiene que retornar una lista de diccionarios pasajeros
    # lista_de_dicc = [{'nombre': 'Rodrigo', 'edad': 31 }]

# Imprimir los datos de los pasajeros del primer colectivo

def carga_pasajero(pasajeros = None): #Indico que el argumento sea opcional inicializando la variable con None

  if pasajeros is None: #si no le paso parametro en la primer llamada me crea la variable con una lista vacía
        pasajeros = []

  datos_nombre = input('Ingresa el nombre del pasajero: ').lower()
  datos_nombre_db = datos_nombre.capitalize()
  datos_edad = int(input('Ingresa la edad del pasajero: '))

  print('<<< PASAJERO CARGADO EXITOSAMENTE >>>')

  datos_pasajero = {'nombre': datos_nombre_db, 'edad': datos_edad} #creo el diccionario que voy a guardar en la lista.

  pasajeros.append(datos_pasajero)

  print('-----------------------------------------------------')

  contunuar_s_n = input('¿Desea cargar otro pasajero? responde con: si/no ')

  if contunuar_s_n.lower() == 'si':
    return carga_pasajero(pasajeros) # llamo a la funcion pero le paso lo que ya se guardo en pasajeros para que no se sobreescriba
  elif contunuar_s_n.lower() == 'no':
    return pasajeros
  else: return 'Opcion incorrecta, vuelva a comenzar'


def solicitud():
  print('<<<< Hola!!! Bienvenido al programa de carga de pasajeros >>>>')

  colectivos = {} #creo el diccionario donde voy a guardar cada colectivo con sus paajeros

  cant_colectivos = int(input('Ingresa la cantidad de colectivos que vas a cargar: '))

  print('-----------------------------------------------------')

  for i in range(1, cant_colectivos+1, 1): #por cada colectivo que quiero cargar me va a pedir los pasajeros
    print(f'INICIA LA CARGA DE PASAJEROS DEL COLECTIVO NÚMERO {i}')
    carga = carga_pasajero()
    colectivos[f'colectivo_{i}'] = carga # como no existe esa propiedad, me la crea con el nombre asignado y le pone como valor la carga de pasajeros
    print(f'El colectivo número {i} fué cargado exitosamente!!')
    print('-----------------------------------------------------')

  colectivo_seleccionado = int(input('Ingresa el número del colectivo del cual deseas traer la lista de pasajeros: '))

  return print(colectivos[f'colectivo_{colectivo_seleccionado}']) # le pido que me traiga el valor del número de colectivo seleccionado


solicitud()