# 1.- Ingresar Dinosaurio
# 2.- Consultar Dinosaurio
# 3.- Actualizar Dinosauro
# 4.- Borrar Dinosaurio
# 5.- Ver estadisticas( mayor peso, y cantidad de dinos)
# 6.- Salir
dinosaurios={}
def ingre():
    nombre=input("ingrese nombre del dinosaurio")
    while True:
        try:
            peso=int(input("ingrese el peso del dinosaurio"))
            break
        except Exception as e:
            print(f"ingrese solo numeros {e}")
    while True:
        tipos=["terrestre", "aereo", "marino", "anfibio"]
        tipo=input("ingrese tipo de dinosaurio terrestre , aereo, marino, anfibio")
        if tipo in tipos:
            print("se ha ingresado el tipo correctamente")
            break
        else:
            print("ingrese un tipo valido")
    ali=input("que tipo de alimentacion tiene?")
    if dinosaurios:
        largo=max(dinosaurios.keys())+1
    else:
        largo=1
    dinosaurios[largo]={
        "nombre": nombre,
        "peso": peso,
        "tipo": tipo,
        "alimentacion": ali
    }
def consul():
    for i, n in dinosaurios.items():
        print(f""" 
              {i}.- 
              nombre:{n["nombre"]}
              peso: {n["peso"]}
              tipo: {n["tipo"]}
              alimentacion: {n["alimentacion"]}""")
def actuali():
    consul()
    act=int(input("ingrese que dinosaurio deseas actualizar"))
    opc=int(input(""""ingrese que desea actualizar:
                  1.- peso
                  2.- tipo
                  3.- alimentacion"""))
    match opc:
        case 1:
            while True:
                try:
                    peso=int(input("ingrese el peso del dinosaurio"))
                    break
                except Exception as e:
                    print(f"ingrese solo numeros {e}")
            dinosaurios[act]["peso"]=peso
        case 2:
            tipo=input("Ingrese el tipo")
            dinosaurios[act]["tipo"]=tipo
        case 3:
            ali=input("Ingrese el alimentacion")
            dinosaurios[act]["alimentacion"]=ali
        case _:
             print("Debe ingresar una opcion valida") 
def borrar():
    consul()
    borrar=int(input("ingrese que dinosaurio deseas borrar"))
    del dinosaurios[borrar]
def estadis():
    listadino=[]
    for i, n in dinosaurios.items():
        listadino.append(n["peso"])
    print(f"peso maximo de los dinosaurio es {max(listadino)}")
    print(f"la cantidad de dinosaurios total es de {len(listadino)}")
while True:
    try:
        op=int(input(""" 
        1.- Ingresar Dinosaurio
        2.- Consultar Dinosaurio
        3.- Actualizar Dinosauro
        4.- Borrar Dinosaurio
        5.- Ver estadisticas( mayor peso, y cantidad de dinos)
        6.- Salir
            """))
        match op:
            case 1:
                ingre()
            case 2:
                consul()
            case 3:
                actuali()
            case 4:
                borrar()
            case 5:
                estadis()
            case 6:
                print("saliendo...")
            case _:
                print("ingrese opcion correcta")
    except Exception as e:
        print({e})



    