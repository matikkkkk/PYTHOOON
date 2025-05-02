claves=[123, 12345, 123456]
saldos=[5000, 10000, 20000]

matias=123
gustavo=12345
ricardo=123456
billete5k=30
billete10k=30
billete20k=30
# print("ESTADO CAJERO")
# print("billetes de 5000", caja5000)
# print("billetes de 10000", caja10000)
# print("billetes de 20000", caja20000)
# total= caja5000*5000 + caja10000*10000 + caja20000*20000
# print("el dinero en caja es de ", total)
nombre=int(input('''ingrese su usuario
                 1. matias
                 2. gustavo
                 3. ricardo'''))
match nombre:
    case 1:
        print("usted ingresó con el usuario matias")
        saldo=saldos[0]
        contraseña1=int(input("ingrese contraseña"))
        while contraseña1!=claves[0]:
            print("intente denuevo")
            contraseña1=int(input("ingrese contraseña"))
        print("usted ingreso como matias y su saldo es de ", saldo)
        montoR=int(input("cuanto desea retirar"))
        if montoR>saldo:
            print("usted no tiene dinero suficiente")
        elif montoR % 5000 !=0:
            print("el numero tiene que ser multiplo de 5000")
        else:
            saldo=saldo-montoR
            print("su saldo actual es")
            cantidad=montoR
            cant20= cantidad//20000
            if cant20>billete20k:
                cant20=billete20k
                cantidad= cantidad - (cant20*20000)

            cant10= cantidad//10000
            if cant10>billete10k:
                    cant10=billete10k
                    cantidad= cantidad - (cant20*10000)



        


     
    case 2:
        print("usted ingresó con el usuario gustavo")
        saldo=saldos[1]
        contraseña2=int(input("ingrese contraseña"))
        while contraseña2!=gustavo:
            print("intente denuevo")
            contraseña2=int(input("ingrese contraseña"))
        print("usted ingreso como gustavo y su saldo es de ", saldo)
        montoR=int(input("cuanto desea retirar"))
 

    case 3:
        print("usted ingresó con el usuario ricardo")
        saldo=saldos[2]
        contraseña3=int(input("ingrese contraseña"))
        while contraseña3!=ricardo:
            print("intente denuevo")
            contraseña3=int(input("ingrese contraseña"))
        
        print("usted ingreso como ricardo y su saldo es de ", saldo)
        montoR=int(input("cuanto desea retirar"))
 





