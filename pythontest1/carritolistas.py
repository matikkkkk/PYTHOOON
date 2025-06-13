productos=["doritos", "papas", "sufles"]
precio=[1000, 1200, 1500]
carrito=[]
total=0
while True:
    opc=int(input("""QUE DESEA HACER
                  1.- AGREGAR PRODUCTOS
                  2.  COMPRAR
                  3.- CREAR BOLETA
                  4.- SALIR """))
    match opc:
        case 1:
            try:
                agre=input("que producto desea agregar? ")
                preci=int(input("ingrese valor del producto" ))
                productos.append(agre)
                precio.append(preci)
                print(f"PERFECTO... USTED AGREGO {agre}: ({preci}) al carrito ")
            except Exception as e:
                print(f"precio invalido. ERROR {e}")
        case 2:
            try:
                for i in range(len(productos)):
                    print(f"{i+1}.-{productos[i]}, {precio[i]} ")   
                comprar=int(input("selecciona el numero del producto que deseas llevar" ))-1
                carrito.append(comprar)
                print(f" se ha agregado {productos[comprar]} al carrito")
            except Exception as err:
                print(f"seleccione un numero.ERROR{err}")
        case 3:
            print("BOLETA")
            for ind in carrito:
                print(f"{productos[ind]}-- {precio[ind]}")
                total+=precio[ind]
            print("---------------------------")    
            print(f"El total a pagar es {total} ")
        case 4:
            print("gracias por usar el carrito")
            break
        case _:
            print("seleccione opcion valida")



            
    