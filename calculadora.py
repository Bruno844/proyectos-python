def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b

#preguntamos que eliga la operacion
while True:
    try:
        operacion = float(input("seleccione la operacion: ""\n1.suma\n2.resta\n3.multiplicacion\n4.division\n"))
        if(operacion <= 4 and operacion >0):
            break
    except:
        print("ingrese un numero")



#operaciones matematicas
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese su segundo numero: "))

if operacion == 1:
    resultado = suma(num1,num2)
elif operacion == 2:
    resultado = resta(num1,num2)
elif operacion == 3:
    resultado = multiplicacion(num1,num2)
elif operacion == 4:
    resultado = division(num1,num2)
else:
    resultado = "operacion no valida"
    print("operacion no valida")


print("resultado: ", resultado)
