import random


def adivina_el_num_computadora(x):
    print('===============')
    print('bienvenido al juego')

    print(f"selecciona un numero entre 1 y {x} para que la compu lo adivine")

    limite_inferior = 1
    limite_superior = x 

    respuesta_usuario = ""
    while respuesta_usuario != "c":
        #generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior

        #obtener una respuesta del usuario
        respuesta_usuario = input(f"Mi prediccion es {prediccion }. Si es alta, ingresa (A), si es baja ingresa (b), si es correcta ingresa (C):  ").lower()

        if respuesta_usuario == "a":
            limite_superior = prediccion - 1 #de esa manera vamos reduciendo el intervalo
        elif respuesta_usuario == "b":
            limite_inferior = prediccion + 1

    print(f"la compu adivino tu numero correctamente!: {prediccion}")


adivina_el_num_computadora(10)