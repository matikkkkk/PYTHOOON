saldo=100000
compra=0
import time
def pagotarjeta():
    global saldo
    while True:
        print("INGRESANDO AL PAGO DE CUPO")
        print("----------------------------")
        print(f"usted tiene una deuda de: {saldo}")
        try:
            pagodeu=int(input("ingrese un monto para pagar deuda de la tarjeta"))
            if pagodeu<=0:
                print("el monto ingresado debe ser mayor o igual a 0")
            elif pagodeu>saldo:
                print("el monto ingresado es mayor al de la tarjeta")
            else:
                saldo-=pagodeu
                print(f"PAGO EXITOSO SU  SALDO ES DE {saldo} ")
                break
        except ValueError as er:
            print(f"ingrese el numero correctamente error : {er} ")
def compras():
    global compra, saldo
    while True:
        time.sleep(1)
        try:
            compra=int(input(f"INGRESE EL PRECIO DE la COMPRA "))
            if compra>=0:
                saldo+=compra
                print("COMPRA EXITOSA")
                otra=int(input('''desea hacer otra compra? 
                            1.- si 
                            2.- no'''))
                if otra!=1:
                    break    
            else:
                print("el monto de la compra debe ser mayor o igual a 0. intente denuevo")
        except ValueError as er:
            print(f"ingrese el numero correctamente error : {er} ")           
def menutar():
    while True:
        try:
            op=int(input('''Opciones disponibles de tarjeta...
                            1.- pagar
                            2.- comprar
                            3.- salir
                        '''))
            match op:
                case 1:
                    print("ingresando a Pagar...")
                    time.sleep(1)
                    pagotarjeta()
                case 2:
                    print("ingresando a compras...")
                    time.sleep(1)
                    compras()
                case 3:
                    print("Gracias por su atencion...")
                    break
                case _:
                    print("ingrese opcion valida")
        except ValueError as er:
            print(f"ingrese el caracter correctamente error : {er} ")        
            
menutar()







