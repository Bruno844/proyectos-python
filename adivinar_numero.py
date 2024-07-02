import random

def adivina_el_numero(x):

    print("==========================")
    print("  bienvenido/a al juego  ")
    print("==========================")
    print("tu meta es adivinar el numero generado por la computadora!")

    #numero aleatorio entre 1 y x
    numero_aleatorio = random.randint(1,x)

    prediccion = 0

    while prediccion != numero_aleatorio:
        #usuario ingresa un num
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("intenta otra vez,este numero es muy pequeño") 
        elif prediccion > numero_aleatorio:
            print("es mayor el numero, prueba de nuevo!")
    
    print(f"felicidade4s, adivinaste el numero {numero_aleatorio} correctamente")


adivina_el_numero(10)
