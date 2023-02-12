
import os
import random

def run():
    imagenes = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''']

    db = ('hormiga mandril murcielago oso castor camello gato almeja cobra puma \
            coyote cuervo ciervo perro burro pato aguila loro zorro rana cabra \
            ganso halcon leon lagarto llama topo mono alce raton mula \
            nutria buho panda papagayo paloma piton conejo rata \
            rinoceronte salmon foca tiburon oveja zorrino perezoso vibora araña \
            cigueña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo \
            salmon cebra').split()

    palabra = random.choice(db)
    espacios = ['_'] * len(palabra)
    intentos = 0

    while True:
        os.system('clear')
        for letra in espacios:
            print(letra, end=" ")
        print(imagenes[intentos])
        ingreso = input('Elige una letra: ')

        acierto = False
        for idx, letra in enumerate(palabra):
            if letra == ingreso:
                espacios[idx] = ingreso
                acierto = True

        if not acierto:
            intentos +=1

        if '_' not in espacios:
            os.system('clear')
            print('GANASTE!!!')
            break

        if intentos == 6:
            os.system('clear')
            print('PERDIDTE!!!')
            break

if __name__=='__main__':
    run()