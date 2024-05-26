"""
El objetivo consiste en desarrollar el juego interactivo “adivina la palabra”.
El funcionamiento esperado es el siguiente:
Al ejecutar el programa se mostrará por pantalla una palabra oculta usando tantos guiones
como letras contiene la palabra a adivinar(la palabra a adivinar será elegida por el
programa usando el módulo de Python random), la cantidad de vidas con las que cuenta el
jugador y las cantidad de letras incorrectas que va ingresando.
Cuando el jugador ingresa una letra es necesario que se valide el dato( que sea una letra).
Luego de validar la letra ingresada se corrobora si la letra ingresada pertenece a alguna de
las letras de la palabra a adivinar.
Cada vez que el jugador ingrese una letra que NO pertenece a la palabra a adivinar se
restará una vida.
El juego finaliza cuando el jugador queda sin vidas o cuando adivina todas las letras de la
palabra. Para todos los casos se debe mostrar un mensaje indicando si ganó la partida o si
perdió. 
"""
import random

words = ['alambre', 'martillo', 'armario', 'elefante', 'camisa', 'empaquetar', 'alcohol']

#Bienvenida
welcome = lambda:    print('Bienvenido al juego: "EL AHORCADO"\n'
      '\n'
      'Objetivo del juego:\n'
      'Debes adivinar la palabra oculta.\n'
      '\n'
      'Cómo jugar:\n'
      '1. Tienes 5 oportunidades para adivinar la palabra.\n'
      '2. Ingresa una letra cada vez.\n'
      '3. Si la letra está en la palabra, se mostrará su posición.\n'
      '4. Si la letra no está, perderás una oportunidad.\n'
      '5. Si pierdes todas las oportunidades, tendrás que empezar de nuevo.\n'
      '\n'
      '❤❤❤❤❤❤¡¡¡Mucha suerte!!!❤❤❤❤❤❤\n')

#logica para restar vidas
def lifes(count, acert):
    if not acert:
        count -= 1
        print(f'Haz perdido una oportunidad, tienes {count} vidas restantes')
    else:
        print('Felicitaciones, haz acertado la letra, sigue así')
        
    if count == 0:
        print('Ya no tienes vidas. Vuelve a comenzar el juego')
        
    return count

# Crear una nueva palabra donde los caracteres no presentes en 'character' son reemplazados por '-'
def word_incognit(word, visible_character):
    new_word = ''.join([
                        char if char in visible_character else '-' 
                        for char in word
                        ])
    return new_word
    """
        Devuelve una nueva palabra donde los caracteres no presentes en 'caracteres_visibles'
        son reemplazados por '-'.

        :param word: La palabra original a ser transformada.
        :param visible_character: Una colección de caracteres que deben permanecer visibles en la palabra.
        :return: La nueva palabra con caracteres ocultos.
        """

def start_game():
    random_word = random.choice(words) #guarda la palabra escondida
    correct_letters = set()            #crea un conjunto para almacenar las letras que el jugador ha adivinado correctamente evita duplicados
    incorrect_letters = []             #guarda las letras erroneas
    lives = 5                          #vidas iniciales
    word_length = len(random_word)     #cantidad de letras
    
    welcome()
    
    print(f'LA PALABRA CONTIENE {word_length} LETRAS')
    
    #bucle que ejecutará la dinamica, si tengo al menos una vida el juego se vuelve a ejecutar
    while lives > 0:              
        print(word_incognit(random_word, correct_letters))
        char_param = input('Elije una letra: ')
        
    #si no es una string o es un numero o caracter especial da error pero concleartínua con el bucle
        if not isinstance(char_param, str) or len(char_param) != 1 or not char_param.isalpha(): 
            print("ERROR: El dato debe ser una letra.")
            continue #permite que vuelva a pedir una nueva letra sin continuar con la lógica actual, que depende de tener una entrada válida
    
    #verifica si ya se uso la letra tanto en el conjunto de acertadas como de erroneas
        if char_param in correct_letters or char_param in incorrect_letters:
            print(f'Ya has intentado con la letra "{char_param}". Intenta con otra.')
            continue #Hara que el código dentro del bucle no se ejecutará para esta iteración, y el programa volverá a pedir al usuario que ingrese una nueva letra.
        
        if char_param in random_word: #verifica si la letra esta en la palabra
            correct_letters.add(char_param) #la suma a las letras adivinadas
            print(f'¡Bien hecho! La letra "{char_param}" está en la palabra.')
            if set(random_word) == correct_letters: # verifica si todas las letras fueron adivinadas
                print(f'¡Felicidades! Has descubierto la palabra: {random_word}')
                break #finaliza el bucle
        else:
            incorrect_letters.append(char_param)
            print(f'LETRAS ERRÓNEAS HASTA EL MOMENTO: {incorrect_letters}')
            lives = lifes(lives, False)
        
        if lives == 0:
            print(f'Has perdido. La palabra era: {random_word}')
            break
    
    if input('¿Quieres jugar de nuevo? (s/n): ').lower() == 's':
        start_game()

start_game()