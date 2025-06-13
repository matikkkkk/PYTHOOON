#uso y explicacion del match
import time
import random
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
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print("el resultado de la division es: ", n1/n2)

def calcu():
    while True:
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

def prom():

    print("ingrese 3 notas")

    n1=float(input())
    n2=float(input())
    n3=float(input())
    prom=(n1+n2+n3)/3
    print("el promedio de", n1, n2, n3 ,"es", round(prom, 2))

    if prom>=40:
        print("el estudiante aprobó")
    else:
        print("el estudiante reprobó")
        

def ins():
    costo=random.randint(4000, 30000)
    print("inscripcion de nacimientos")
    print(input("ingrese el nombre "))
    print(int(input("ingrese el numero de nacimiento ")))
    print("Inscripción completada.")
    time.sleep(1)

def matri():
        costo=random.randint(4000, 30000)
        print("Inscripción de matrimonio")
        nom3 = input("Ingrese el primer nombre: ")
        doc2 = input("Ingrese RUT: ")
        nom4 = input("Ingrese el segundo nombre: ")
        doc3 = input("Ingrese RUT: ")
        print("Matrimonio registrado.")
        time.sleep(1)

def profes():
    costo=random.randint(4000, 30000)
    print("Inscripción de profesión")
    prof = input("Ingrese su profesión: ")
    print("su inscripcion esta a nombre de ", prof)
    time.sleep(1)

def cedul():
    costo=random.randint(4000, 30000)
    print("Cédula para extranjeros")
    pasa = input("Ingrese número de pasaporte: ")
    pais = input("Ingrese país de origen: ")
    print("Inscripción completada.")
    time.sleep(1)

def nomape():
    costo=random.randint(4000, 30000)
    print("Cambio de nombre y apellidos")
    nom5 = input("Ingrese su nuevo nombre (o el actual si no cambia): ")
    apelli = input("Ingrese su nuevo apellido (o el actual si no cambia): ")
    print("Su nuevo nombre es ", nom5, apelli)
    time.sleep(1)

def registro(): 
    maxP=500
    maxL=100
    GenteT=0
    GananciaT=0
    while GenteT<2: #se debe cambiar para que sean 500 pero esto es para probar
        if GenteT>=maxL: #esto es para no dejar esperando a mas de 100 personas
            print("Límite de personas en espera alcanzado.")
            break

        print("bienvenido al sistema")
        time.sleep(1)
        rut=input("ingrese su rut ")

        print("esperando...")
        time.sleep(1)

        print("\n" *10)
            
        nombre=input("ingrese su nombre ")
        print("Hola " + nombre + ", bienvenido al registro civil.")
        print("¿Qué trámite viene a hacer?")
        print("1. Inscripción de nacimientos")
        print("2. Inscripción de matrimonios")
        print("3. Inscripción de profesionales")
        print("4. Inscripción de cambios de nombre y apellidos")
        print("5. Inscripción de cédulas de identidad para extranjeros")
        print("6. Salir")
        op=int(input("elija opcion "))
        if op == 6:
                break
        costo=random.randint(4000, 30000)
        time.sleep(1)
        match op:
            case 1:
                ins()
                print("listo, sus resultados seran enviando al correo")
                print("pase a pagar sus costos son ", costo)
            case 2:
                matri()
                print("listo, sus resultados seran enviando al correo")
                print("pase a pagar sus costos son ", costo)
            case 3:
                profes()
                print("listo, sus resultados seran enviando al correo")
                print("pase a pagar sus costos son ", costo)
            case 4:
                nomape()
                print("listo, sus resultados seran enviando al correo")
                print("pase a pagar sus costos son ", costo)
                
            case 5:
                cedul()
                print("listo, sus resultados seran enviando al correo")
                print("pase a pagar sus costos son ", costo)
                
        GananciaT+=costo
        GenteT+=1
        print("el resultado de ganancia del dia de hoy es", GananciaT )

registro()



        
        
        
