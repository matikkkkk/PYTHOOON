claves=[123, 12345, 123456]

billete5k=30
billete10k=30
billete20k=30
while True:

    nombre=int(input('''ingrese su usuario
                    1. matias
                    2. gustavo
                    3. ricardo
                    4.- Salir'''))
    match nombre:
        case 1:

            print("usted ingresó con el usuario matias")  
            contraseña1=int(input("ingrese contraseña"))
            while contraseña1!=claves[0]:
                print("intente denuevo")
                contraseña1=int(input("ingrese contraseña"))

        case 2:
            print("usted ingresó con el usuario gustavo")
            contraseña2=int(input("ingrese contraseña"))
            while contraseña2!=claves[1]:
                print("intente denuevo")
                contraseña2=int(input("ingrese contraseña"))

        case 3:
            print("usted ingresó con el usuario ricardo")
            contraseña3=int(input("ingrese contraseña"))
            while contraseña3!=claves[2]:
                print("intente denuevo")
                contraseña3=int(input("ingrese contraseña"))
        case 4:
            print("Saliendo...")
            break
    saldocajero= (billete5k*5000)+(billete20k*20000)+(billete10k*10000)    
    print("saldo disponible en el cajero ", saldocajero)
    montor=int(input("cuanto dinero desea retirar"))
    if montor>saldocajero:
        print("no hay suficiente dinero")
    elif montor % 5000 != 0:
        print("el numero debe ser multiplo de 5000")
    else:
        cantidad=montor
        cant20=min(cantidad//20000, billete20k)
        cantidad-=cant20*20000

        cant10 = min(cantidad // 10000, billete10k)
        cantidad -= cant10 * 10000

        cant5 = min(cantidad // 5000, billete5k)
        cantidad -= cant5 * 5000
        if cantidad==0:
            billete10k-=cant10
            billete20k-=cant20
            billete5k-=cant5
            saldo_cajero = billete5k * 5000 + billete10k * 10000 + billete20k * 20000
            print("se retiro exitosamente el dinero, los billetes que se usaron fueron: ")
            if cant20>0:
                print("se usaron", cant20, "de 20000 ")
            if cant10>0:
                print("se usaron", cant10, "de 10000 ")  
            if cant5>0:
                print("se usaron", cant5, "de 5000 ")     
            print("Saldo restante en el cajero: $", saldo_cajero)
        else:
            print("no se pudo entregar el monto exacto con los billetes que hay")

            #Falto el tema del bucle, sin tener que iniciar sesion todo el tiempo





  

            
 





