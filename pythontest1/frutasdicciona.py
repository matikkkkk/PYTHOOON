frutas={
    "frutas":[]


}

while True:
    opc=int(input("""
                  1.- ingresar fruta y precio
                  2.- actualizar precio
                  3.- borrar fruta y precio
                  4.- mostrar todas las frutas y precios
                  5.- salir : """))
    match opc:
        case 1:
            fru=input("ingrese fruta")
            precio=int(input("ingrese precio"))
            frutas[fru]=precio
        case 2:
            frutasActuali=input("ingrese fruta")
            frutas[]