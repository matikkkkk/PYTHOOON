import time
import random
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
    if op==1:
           print("inscripcion de nacimientos")
           print(input("ingrese el nombre "))
           print(int(input("ingrese el numero de nacimiento ")))
           print("Inscripción completada.")
           time.sleep(1)
           print("listo, sus resultados seran enviando al correo")
    elif op==2:
                print("Inscripción de matrimonio")
                nom3 = input("Ingrese el primer nombre: ")
                doc2 = input("Ingrese RUT: ")
                nom4 = input("Ingrese el segundo nombre: ")
                doc3 = input("Ingrese RUT: ")
                print("Matrimonio registrado.")
                time.sleep(1)
                print("listo, sus resultados seran enviando al correo")
    elif op==3:
                print("Inscripción de profesión")
                prof = input("Ingrese su profesión: ")
                print("su inscripcion esta a nombre de ", prof)
                time.sleep(1)
                print("listo, sus resultados seran enviando al correo")
    elif op==4:
                print("Cambio de nombre y apellidos")
                nom5 = input("Ingrese su nuevo nombre (o el actual si no cambia): ")
                apelli = input("Ingrese su nuevo apellido (o el actual si no cambia): ")
                print("Su nuevo nombre es ", nom5, apelli)
                time.sleep(1)
                print("listo, sus resultados seran enviando al correo")
    elif op==5:
                print("Cédula para extranjeros")
                pasa = input("Ingrese número de pasaporte: ")
                pais = input("Ingrese país de origen: ")
                print("Inscripción completada.")
                time.sleep(1)
                print("listo, sus resultados seran enviando al correo")
                print("pase a pagar sus costos son ", costo)
    else:
        print("Opción no válida. Intente nuevamente.")
    GananciaT+=costo
    GenteT+=1
print("el resultado de ganancia del dia de hoy es", GananciaT )

                 



     

