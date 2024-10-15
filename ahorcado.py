from palabras import palabras
from ahorcado_diagrama import vidas_diccionario_visual
import string
import random

def obtener_palabra_valida(palabras):
    #seleccionaruna palabra x de la lista
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    return palabra


def ahorcado():

    print("================================")
    print("bienvenido al juego del ahorcado")
    print("================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set() 
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"tequedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        #mostrar el edtado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        #mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        #mostrar las letras separadas por un espacio con el join
        prin(f"palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("escoge una letra: ").upper()

        #si la letra escogida por el usuario esta en el abecedario y no esta en el conjunto de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #si letra esta en la palabra
            #quitar la letra del conjunto de letras pendientes por adivinar
            #si no esta en la palabra, quitar una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"tu letra, {letra_usuario} no esta en la palabra")
        #si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print('ya escogiste esa letra, pruebe con otra')
        else:
            print("eliga una letra valida")

    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print('perdiste,lo siento')
    else:
        print(f"ganaste!!! bien hecho,la palabra es {palabra}")


ahorcado()