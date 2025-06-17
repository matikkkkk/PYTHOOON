# def suma ():
#     n1=int(input("ingrese un num"))
#     n2=int(input("ingrese un num"))
#     print(n1+n2)
# def suma_ret_arg(n1, n2):
#     return(n1+n2)
# print(suma_ret_arg(10,3))

# def iva(n):
#     return n*0.19
# print(iva(1000))

# def desc(precio, porcentaje):
#     return precio*porcentaje/100
# print(desc(1000,20))

# neto=10000
# print(f"El IVA ES {iva(neto)}")
# print(f"el precio total es {iva(neto)+neto}")
# productos=[
#     {"nombre": "leon","precio" : 4400},
#     {"nombre": "goma","precio" : 200}

# ]
# print(productos[1]["nombre"])
productos=[
    {}
]
while True:
    try:
        op=int(input("""
                        1.- agregar prod
                        2.- borrar
                        3.- actualizar
                        4.- mostrar
                        5.- salir"""))
    except Exception as e:
        print(f"ERROR{e}")
        continue
    match op:
        case 1:
            try:
                articulo=input("ingrese el nombre de su articulo")
                preci=int(input("ingrese el precio"))
                productos.insert(0,{"nombre":articulo, "precio": preci})
            except Exception as err:
                print(f"ERROR.{err}")    
        case 2:
            try:

                for i in range (len(productos)):
                    print(f"{i+1} {productos[i]}")
                borr=int(input("ingrese numero"))-1
                print(f"se ha eliminado correctamente el articulo{borr}")
                productos.pop(borr)
            except Exception as a:
                print(f"ERROR. {a}")
        case 3:
            try:
                print("producto y precios")        
                for i in range(len(productos)):
                    print(f"{i+1} {productos[i]}")
                actua=int(input("ingrese que producto quiere actualizar"))
                productos[actua-1]["nombre"]=input("ingrese nuevo nombre")
                productos[actua-1]["precio"]=int(input("ingrese nuevo precio"))
            except Exception as p:
                print(f"ERROR.{p}")         
        case 4:
            print("producto y precios")        
            for i in range(len(productos)):
                print(f"{i+1} {productos[i]}")
        case 5:
            print("saliendo...")
            break
        case _: 
            print("ingrse opcion valida")