entradas={}

def codigo(cod):
    mayus=0
    digi=0
    for palabra in cod:
        if palabra.isdigit():
            digi+=1
        if palabra.isupper():
            mayus+=1    
    if len(cod)>=6 and mayus>=1 and digi>=1 and not " " in cod:
        return True
    else:
        return False
def tipos(tipo):
    if tipo in ["C", "V"]: 
        return True
def repetir(nombre, entradas):
    for datos in entradas.values():
        if datos["nombre"]== nombre:
            return False
        return True
def comprara():
    global entra
    nombre=input("ingrese nombre del comprador")
    if repetir(nombre, entradas):
        print("nombre ingresado correctamente")
    else:
        print("el nombre ya existe")
        return
  
    tipo=(input("ingrese tipo de entrada (C/V)"))
    if tipos(tipo):
        print("tipo ingresado correctamente")
    else:
        print("solo debe ser C O V")
        return
    cod=(input("ingrese codigo  debe tener largo mínimo de 6 caracteres, debe tener al menos 1 letra mayúscula, al menos 1 número y no puede tener espacio en blanco"))
    if codigo(cod):
        print("codigo ingresado correctamente")
    else:
        print("codigo invalido")
        return
    if entradas:
        largo=max(entradas.keys())+1
    else:
        largo=1
    entradas[largo]={
        "nombre": nombre,
        "tipo": tipo,
        "codigo":cod
    }
def consul():
    global entradas
    consultar=input("ingrese el nombre")
    for d in entradas:
        if consultar in entradas[d]["nombre"]:
            print("COMPRADOR ENCONTRADO: ")
            print(f"nombre: {entradas[d]['nombre']}, tipo: {entradas[d]['tipo']}, codigo: {entradas[d]['codigo']}")
            return True
    return False
def cancel():
    global entradas
    cancel=input("ingrese el nombre del comprador que desea eliminar")
    for i in entradas:
        if cancel in entradas[i]["nombre"]:
            print("COMPRADOR ENCONTRADO: ")
            print(f"nombre: {entradas[i]['nombre']}, tipo: {entradas[i]['tipo']}, codigo: {entradas[i]['codigo']}")
            print("eliminando comprador")
            del entradas[i]
            return True
    return False
while True:
    try:
        opc=int(input("""MENU PRINCIPAL
                        1.- Comprar entrada.
                        2.- Consultar comprador.
                        3.- Cancelar compra.
                        4.- Salir. """))
        match opc:
            case 1:
                comprara()
            case 2:
                for i, d in entradas.items():
                    print(i, d)
                if consul():
                    print("")
                else:
                    print("comprador no encontrado")
            case 3:
                if cancel():
                    print("")
                else:
                    print("el comprador no se encuentra")
            case 4:
                print("saliendo. Programa terminado...")
                break
            case _:
                print("ingrese opcion valida")
    except Exception as e:
        print({e})
            