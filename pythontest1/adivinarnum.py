import random
op=0
num=random.randint(1, 50)
cantidadInt=10
intentos=1
cantint2=10
while op!=num and intentos<=cantidadInt:
    print("tiene", cantint2, "intentos")
    op=int(input("adivine el numero correcto ingresandolo "))
    intentos+=1
    cantint2-=1
    if op<num:
        print("el numero correcto es mayor al que pusiste")
    elif op>num:
        print("el numero correcto es menor al que pusiste")
    else:
        print("adivinaste el numero")
if op!=num:
    print("has llegado al limite de intentos")













