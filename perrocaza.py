import random
import time
cuotm=3
cumplieron=0
nocumplieron=0
while True:
    try:
        perros=int(input("cuantos perros tiene: "))
        while perros<1:
            print("ingrese 1 o mas perros")
            perros=int(input("cuantos perros tiene: "))
            for i in range(perros):
                    print("la cuota minima de conejos para cazar es de", cuotm)
                    print("-------------------------------------------------")
                    print("... sale a cazar el perro nro ", i+1)
                    time.sleep(1)
                    conejosca=random.randint(0,8)
                    print(f"el perro nro {i+1} a cazado la cantidad de {conejosca} de conejos")
                    time.sleep(2)
                    if conejosca>=cuotm:
                        print("obtiene tiene filete")
                        cumplieron+=1
                    else:
                        print("no obtiene tiene filete")
                        nocumplieron+=1          
        print("----------------------------------------------------------")
        print(f"Los perros que cumplieron con traer filete son {cumplieron}")
        print(f"Los perros que no cumplieron con traer filete son {nocumplieron}")
        break
    except ValueError as error1:
        print("error, ingresó un caracter invalido:", error1) 


    


