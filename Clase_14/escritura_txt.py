"""Tengo que indicarle la rura del archivo y la forma en la que voy a interactuar"""

#de esta forma lo sobreescribe
with open("./datasets/txt_lectura.txt", mode="w") as f:
    print(f.write("sobreescribiendo en mi archivo existente")) 


#si no existe lo crea  
with open("./datasets/txt_lectura2.txt", mode="w") as f:
    print(f.write("creando un nuevo archivo")) 
    
#Le suma una linea a lo existente
with open("./datasets/txt_lectura2.txt", mode="a") as f:
    print(f.write("\nesta es una nueva línea")) 
    
#ejemplo ingresar texto por input

with open("./datasets/txt_lectura3.txt", mode="a") as f:
    texto = input('Ingrese su comentario aqui: ')
    print(f.write(texto)) 