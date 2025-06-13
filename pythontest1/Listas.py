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
# productos = []
# while True:
#     try:
#         opc=int(input('''
#                         1.- agregar 
#                         2.- eliminar
#                         3.- mostrar
#                         4.- salir'''))
#     except ValueError as e:
#         print(f"ERROR.{e} ")
#     match opc:
#         case 1:
#                 nombreProducto = input("ingrese nombre del producto")
#                 productos.append(nombreProducto)
#                 print(productos)  
#         case 2:
#                 cont= 1
#                 for i in productos:
#                       print(f"{cont}.- {i}")
#                       cont+=1
#                 eliminarProducto=int(input("cual desea eliminar?"))-1
#                 productos.pop(eliminarProducto)
#         case 3:
#                 cont=1
#                 for i in productos:    
#                     print(f"{cont}.- {i}")
#                     cont+=1
#         case 4:
#                 print("gracias por su atencion...")
#                 break
#         case _:
#                 print("seleccione una opcion valida")

# numeros=[1,2,3,4]
# for numero in numeros:
#     print("nota:", numero)
# num=int(input("ingrese un num"))
# numeros.append(num)
# print(numeros)
nombres=[]
apellidos=[]
while True:
    print('''
        1.- ingresar nombre
        2.- buscar nom
        3.- mostrar nomb¿ y apellidos
        4.- salir
        ''')
    op=int(input("selecciones op"))
    match op:
        case 1:
            nom=input("ingrese un nom")
            ape=input("ingrese un apellido")
            nombres.append(nom)
            apellidos.append(ape)
        #print(apellidos)
        case 2:
            busca=input("ingrese nombres a buscar")
            if busca in nombres:
                print(f"el nombre {busca} existe en la lista")
            else:
                print(f"el nombre {busca} no existe en la lista")
        case 3:
            cont=1
            for napelli in nombres and apellidos:
                print(f"{cont}: {nombres[cont-1]} {apellidos[cont-1]}")
                cont+=1
        case 4:
            print("saliendo")
            break
        case _:
            print("opcion no valida")