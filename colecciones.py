# miLista=[1,2,3,4,5]
# miLista.append(7)
# for elementos in miLista:
#     print(elemento

# miLista=[1,2,3,4,5]
# miLista.insert(3, "juan")
# for elementos in miLista:
#     print(elementos)
# diccionario={"nombre": "cesar ccc", 
#     "fonos": [
#             2222222,
#             222222,
#             22222],

#     "activo" : True}

# productos = []
# for i in range (5):
#     nombreProducto = input("ingrese nombre del producto")
#     productos.append(nombreProducto)
# print(productos)  
productos = []
while True:
    try:
        opc=int(input('''
                        1.- agregar 
                        2.- eliminar
                        3.- mostrar
                        4.- salir'''))
    except ValueError as e:
        print(f"ERROR.{e} ")
    match opc:
        case 1:
                nombreProducto = input("ingrese nombre del producto")
                productos.append(nombreProducto)
                print(productos)  
        case 2:
                cont= 1
                for i in productos:
                      print(f"{cont}.- {i}")
                      cont+=1
                eliminarProducto=int(input("cual desea eliminar?"))-1
                productos.pop(eliminarProducto)
        case 3:
                cont=1
                for i in productos:    
                    print(f"{cont}.- {i}")
                    cont+=1
        case 4:
                print("gracias por su atencion...")
                break
        case _:
                print("seleccione una opcion valida")