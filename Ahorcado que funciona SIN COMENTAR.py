#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import choice

print("\n")
print("¡Bienvenido al juego del Ahorcado!\n")
print("Intenta adivinar la palabra oculta antes de que se acaben tus vidas.\n")
print("Tienes 6 vidas.\n")
print("¡Buena suerte!\n")

palabras = ['adalab', 'sql', 'analytics', 'data']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_de_palabra = len(set(palabra_elegida))

    return palabra_elegida, letras_de_palabra


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = "abcdefghijklmnñopqrstuvwyz"

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("Solo puedes introducir letras.")

    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

    if intentos == 6:
        print("  ___")
        print(" |       |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
        
    elif intentos == 5:
        print("  ___")
        print(" |       |")
        print(" |       O")
        print(" |")
        print(" |")
        print("_|_")
    elif intentos == 4:
        print("  ___")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" |")
        print("_|_")
    elif intentos == 3:
        print("  ___")
        print(" |       |")
        print(" |       O")
        print(" |      /|")
        print(" |")
        print("_|_")
    elif intentos == 2:
        print("  ___")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |")
        print("_|_")
    elif intentos == 1:
        print("  ___")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |      /")
        print("_|_")
    


def comprobar_letra(letra_elegida, palabra_oculta, vidas, aciertos, letras_de_palabra):

    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        aciertos += 1
        print('¡Muy bien, has acertado una letra, sigue así!')
    
    elif letra_elegida in letras_incorrectas or letra_elegida in letras_correctas:
        print("Ya introdujiste esta letra.")
        
    else:
        print(f"Vaya la letra introducida no es correcta, tienes {vidas - 1} vidas.")
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif aciertos == letras_de_palabra:
        fin = ganar(palabra_oculta)

    return vidas, fin, aciertos



def perder():
    print("  ___")
    print(" |       |")
    print(" |       O")
    print(" |      /|\\")
    print(" |      / \\")
    print("_|_")
    print("Te has quedado sin intentos.")
    print("La palabra oculta era " + palabra)
    print("Si quires jugar otra vez, dale al play.")
    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("¡¡¡Enhorabuena, has encontrado la palabra oculta!!!")

    return True


palabra, letras_de_palabra = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos, terminado, aciertos = comprobar_letra(letra, palabra, intentos, aciertos, letras_de_palabra)

    juego_terminado = terminado


# In[ ]:




