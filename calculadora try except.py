def suma():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print("el resultado de la suma es: ", n1+n2)

def resta():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print("el resultado de la resta es: ", n1-n2)

def multi():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print("el resultado de la multiplicacion es: ", n1*n2)
    
def divi():
    try:
        n1=int(input("ingrese un numero: "))
        n2=int(input("ingrese otro numero: "))
        print("el resultado de la division es: ", n1/n2)
    except ZeroDivisionError as nombre_de_excepcion:
        print(f"Se produjo una excepción: {nombre_de_excepcion}")

def calcu():
    while True:
        try:
            op=int(input('''ingrese una operacion
                        1.- suma
                        2.- resta 
                        3.- multiplicacion
                        4.- division
                        5.- salir
                        '''))
            match op:
                case 1:
                    print("suma")
                    suma()
                case 2:
                    print("resta")
                    resta()
                case 3:
                    print(" multiplicacion")
                    multi()
                case 4: 
                    print("division")  
                    divi()
                case 5:
                    print("saliendo...")
                    break
                case _:
                    print("opcion invalida")
        except ValueError as mati:
            print("error:", mati)

