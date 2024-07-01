import string
import random


def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(longitud):
        password += random.choice(caracteres)
    return password

longitud = int(input("cual es la longitud de la contraseña deseada: " ))
12
nueva_password = generar_password(longitud)
print("la nueva contraseña es: ",nueva_password)

