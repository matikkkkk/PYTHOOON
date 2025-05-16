import time
preciototal=0
cantar=0
nombre="cliente"
while True:
    try:
        opc=int(input('''que desea hacer
                    1.- ingresar nombre (será mostrado en la boleta)
                    2.- comprar
                    3.- pedir boleta(salir)
                    '''))
        match opc:
            case 1:
                nombre=(input("ingrese su nombre"))
                print("su nombre se asignó como: ", nombre)
            case 2:
                try:
                    while True:
                        op=int(input('''que productos desea llevar
                                    1.- galletas(2.000)
                                    2.- gorro(4.000)
                                    3.- chaqueta(7.000)
                                    4.- zapato(10.000)
                                    5.- volver al menu
                                    
                                    '''))
                        match op:
                            case 1:
                                print("usted lleva unas galletas")
                                preciototal+=2000
                                cantar+=1
                            case 2:
                                print("usted lleva un gorro")
                                preciototal+=4000
                                cantar+=1
                            case 3: 
                                print("usted lleva una chaqueta")
                                preciototal+=7000
                                cantar+=1
                            case 4: 
                                print("usted lleva un zapato")
                                preciototal+=10000
                                cantar+=1
                            case 5:
                                print("volviendo al menu...")
                                break
                            case _:
                                print(" error ingrese numero correcto")   
                except ValueError as error1:
                     print("error, ingresó un caracter invalido:", error1)
            case 3:
                if cantar<3:
                    print("debe llevar al menos 3 articulos")
                else:
                    print("-----BOLETA -----")
                    print("hola ", nombre, "espero que este bien, los totales fueron: ")
                    time.sleep(1)
                    print("Su total de productos en el carro fueron", cantar)
                    print("el precio total neto es de ", preciototal)
                    print("el precio mas el iva es de ", preciototal*1.19)
                    break
            case _:
                print(" error ingrese numero correcto")
    
    except ValueError as error:
        print("error, ingresó un caracter invalido: ", error)


        
            

