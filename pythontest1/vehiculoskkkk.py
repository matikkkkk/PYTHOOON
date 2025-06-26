#Crear gestion de vehiculos
#Crear programa para un parking de autos
#se debe ingresar
#Marca, año, patente, Tipo

#Marca: tipo string, se debe tipear la marca
#año: tipo int , solo de 4 digitos enteros
#patente: debe tener 4 letras minusculas y 2 digitos
#tipo: S= sedan, C= Camioneta, M= moto

#Se debe validar cada aspecto y tener un mantenedor para 
#todos los vehiculos motorizados

#1.- Ingresar Vehiculo
#2.- Mostrar Vehiculos
#3.- Actualizar Vehiculo
#4.- Borrar Vehiculo
#5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
#6.- Salir
#Usar dunciones con argumentos para poder validar
#y para poder llamar las acciones dentro del menu
def mostrarauto(ppp):
    for key, value in ppp.items():
        print(key, value)
def borrar(bor):
    mostrarauto(bor)
    borr=int(input("que auto desea borrar?"))
    del bor[borr]
def actuali(actl):
    mostrarauto(actl)
    act=int(input("que auto desea modificar?"))
    while True:
        op=int(input("""que desea modificar?
                    1.- marca
                    2.- año
                    3.- patente
                    4.- tipo
                    5.- salir
                    """))
        match op:
            case 1:
                marca=input("ingrese marca")
                actl[act]["marca"]=marca
            case 2:
                ano=int(input("ingrese año del vehiculo"))
                if anover(ano):
                    print("año ingresado correctamente")
                    actl[act]["año"]=ano
                else:
                    print("año invalido, debe ser de 4 digitos")
                    continue
            case 3:
                paten=input("patente del vehiculo")
                if patens(paten):
                    print("patente ingresada correctamente")
                    actl[act]["patente"]=paten
                else:
                    print("patente invalida, debe tener 4 letras minusculas y 2 digitos")
                    continue

            case 4:
                tipo=input(""" que tipo de vehiculo tienes (s, c Y m )""")
                if tipos(tipo):
                    print("tipo de vehiculo ingresado correctamente")
                    actl[act]["tipo"]=tipo
                else:
                    print("tipo de vehiculo invalido, debe ser S, C o M")
                    continue
            case 5:
                print("saliendo")
                break
def anover(ddd):
    if isinstance(ddd, int) and len(str(ddd)) == 4:
        return True
    else:
        return False
def patens(iii):
    minus=0
    digi=0
    for palabra in iii:
        if palabra.islower():
            minus+=1
        if palabra.isdigit():
            digi+=1
    if minus==4 and digi==2:
        return True
    else:
        return False
def tipos(iii):
    if iii.lower() in ["s", "c", "m"]:
        return True
    else:
        return False   
autos={
    1:{
        "marca": "chevrolet",
        "año": 2015,
        "patente": "dsed34",
        "tipo": "s"
    }
}
while True:
    opc=int(input("""
    1.- Ingresar Vehiculo
    2.- Mostrar Vehiculos
    3.- Actualizar Vehiculo
    4.- Borrar Vehiculo
    5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
    6.- Salir"""))
    match opc:
        case 1:
            marca=input("ingrese marca")
            ano=int(input("ingrese año del vehiculo"))
            if anover(ano):
                print("año ingresado correctamente")
            else:
                print("año invalido, debe ser de 4 digitos")
                continue
            paten=input("patente del vehiculo")
            if patens(paten):
                print("patente ingresada correctamente")
            else:
                print("patente invalida, debe tener 4 letras minusculas y 2 digitos")
                continue
            tipo=input(""" que tipo de vehiculo tienes (s, c Y m )""")
            if tipos(tipo):
                print("tipo de vehiculo ingresado correctamente")
            else:
                print("tipo de vehiculo invalido, debe ser S, C o M")
                continue
            largo=list(autos.keys())[-1]
            autos[largo+ 1] = { 
            "marca": marca,
            "año": ano,
            "patente": paten,
            "tipo": tipo}
        case 2:
            mostrarauto(autos)
        case 3:
            actuali(autos)
        case 4:
            borrar(autos)
        case 5:
            print(f"ulltimo vehiculo ingresado: {autos[list(autos.keys())[-1]]}")
            print(f"total de autos en el garage: {len(autos)}")
        case 6:
            print("saliendo...")
            break
                    
                    



            


        

