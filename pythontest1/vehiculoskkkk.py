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
                ano=input("ingrese ano")
                actl[act]["año"]=ano
            case 3:
                patente=input("ingrese patente")
                actl[act]["patente"]=patente
            case 4:
                tipo=input("ingrese tipo")
                actl[act]["tipo"]=tipo
            case 5:
                print("saliendo...")
                break    
def anover(ddd):
    if isinstance(ddd, int) and len((ddd)) == 4:
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
            paten=input("patente del vehiculo")                                     #patente: debe tener 4 letras minusculas y 2 digitos
                                                                                        #tipo: S= sedan, C= Camioneta, M= moto (ESO ME FALTA(COMPLETAR))
            tipo=input(""" que tipo de vehiculo tienes (S, C Y MOTO)""")
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
                    
                    



            


        

