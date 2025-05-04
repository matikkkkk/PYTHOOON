import random
import time
hp1=50
hp2=50
j1=input("ingrese el nombre del peleador 1: ")
time.sleep(1)
j2=input("ingrese el nombre del peleador 2: ")
turnos=random.randint(1,2)

while hp1>0 and hp2>0:
    if turnos %2==0:
        print("turno de ", j1)
        print("vida de ", j1, [hp1])
        print("/"*hp1)
        ataq=random.randint(3, 15)
        #print(ataq)esto era para ver si funcionaba el crit.
        crit=random.randint(1,4)
        if crit==2:
            ataq*=2
            print("el ataque fue critico de", ataq)
        else: 
            print("el ataque fue normal de", ataq)
        hp2-=ataq
        time.sleep(1)
        print("al vida de ", j2, "es", [hp2])    
        print("/"*hp2)
    else: 
        print("turno de ", j2)
        print("vida de ", j2, [hp2])
        print("/"*hp2)
        ataq=random.randint(1,15)
        #print(ataq)esto era para ver si funcionaba el crit.
        crit=random.randint(1, 4)
        if crit==2:
            ataq*=2
            print("el ataque fue critico de", ataq)
        else:
            print("el ataque fue normal de", ataq)
        hp1-=ataq
        time.sleep(1)
        print("al vida de ", j1, "es", [hp1])    
        print("/"*hp1)
    time.sleep(1)
    turnos+=1

if hp1>hp2:
    print("ha ganado ", j1)
else:
    print("ha ganado ", j2)


    