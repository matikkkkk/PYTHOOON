frutas= {}
while True:
    try:
        opc=int(input("""
                    1.- ingresar fruta y precio
                    2.- actualizar precio
                    3.- borrar fruta y precio
                    4.- mostrar todas las frutas y precios
                    5.- salir : """))
    except Exception as e:
        print(f"ERROR.{e} ingrese opcion correcta")
        continue
    match opc:
        case 1:
            try:
                fru=input("ingrese fruta").lower()
                precio=int(input("ingrese precio"))
                frutas[fru]= precio
            except Exception as er:
                print(f"error {er} ingrese un precio valido")
        case 2:
            if frutas == {}:
                print("no hay ninguna fruta disponibles")
            else:
                try:
                    fru=input("ingrese fruta la cual desea actualizar precio").lower()
                    if fru in frutas:
                        precinuev=int(input(f"ingrese nuevo precio de {fru}"))
                        frutas[fru]=precinuev
                    else:
                        print("esta fruta no esta disponible")
                except Exception as er:
                    print(f"error {er} ingrese un precio valido")            
        case 3:
            frutabor=input("ingrese la fruta que deseas eliminar").lower()
            if frutabor in frutas:
                print("se ha eliminado correctamente...")
                del frutas[frutabor]
            else:
                print("fruta no disponible. no existe")
        case 4:
            print("frutas y precios")
            for fru, precio in frutas.items():
                print(fru, precio)
        case 5:
            print("saliendo...")
            break
        case _:
            print("ingrese opcion valida")

