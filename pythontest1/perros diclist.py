# Ejercicio 6 – Registro de Mascotas por Tipo
# Diccionario con claves como "perros", "gatos", "aves", cada una con una lista de nombres.
# Permite agregar mascota, mostrar por tipo, eliminar por nombre, contar total por tipo y general.
mascotas={
"perros":[],
"gatos":[],
"aves":[]
}
def nombre(dd):
    dig=0
    for i in dd:
        if i.isdigit():
            dig+=1
    if dig==0:
        return True
    else:
        return False                 
def mostrar(dd):
    for i, k in dd.items():
        print(i,k)
def borrarr(dd):
    for tipo in mascotas:
        if dd in mascotas[tipo]:
            mascotas[tipo].remove(dd)
            return True
    print("no esta el nombre en la lista")
    return False
def perrosmos(dd):
    print(dd["perros"])
def gatosmos(dd):
    print(dd["gatos"])
def avesmos(dd):
    print(dd["aves"])
while True:
    try:
        op=int(input("""1.- agregar mascota
                        2.- mostrar por tipo
                        3.- eliminar por nombre
                        4.- contar por tipo y general"""))
    except Exception as e:
        print(f"{e}")
        continue
    match op:
        case 1:
            while True:
                try:
                    tipos=int(input("""que tipo de mascota deseas agregar?
                                    1.- Perros
                                    2.- Gatos
                                    3.- Aves
                                    4.- salir"""))
                except Exception as e:
                    print(f"{e}")
                    continue
                match tipos:
                    case 1:
                        Perros=input("ingrese nombre del perro")
                        if nombre(Perros):
                            print("nombre ingresado")
                            mascotas["perros"].append(Perros)
                        else:
                            print("ingrese nombres solo con letras")
                    case 2:
                        gatos=input("ingrese nombre del gato")
                        if nombre(gatos):
                            print("nombre ingresado")
                            mascotas["gatos"].append(gatos)
                    case 3:
                        aves=input("ingrese nombre del ave")
                        if nombre(aves):
                            print("nombre ingresado")
                            mascotas["aves"].append(aves)
                    case 4:
                        break
                    case _:
                        print("ingrese opcion valida porfavor")
        case 2:
            mostrar(mascotas)
        case 3:
            try:
                opc=int(input("""que tipo de animal desea borrar
                            1.- perros
                            2.- gatos
                            3.- aves"""))
            except Exception as e:
                print(f"{e}")
                continue
            match opc:
                case 1:
                    print("PERROS")
                    perrosmos(mascotas)
                    borrar=input("ingrese nombre de mascota a borrar")
                    if borrarr(borrar):
                        print("removido con exito")
                case 2:
                    print("gatos")
                    gatosmos(mascotas)
                    borrar=input("ingrese nombre de mascota a borrar")
                    if borrarr(borrar):
                        print("removido con exito")
                case 3:
                    print("aves")
                    avesmos(mascotas)
                    borrar=input("ingrese nombre de mascota a borrar")
                    if borrarr(borrar):
                        print("removido con exito")
        case 4:
            perros=len(mascotas["perros"])
            gatos=len(mascotas["gatos"])
            aves=len(mascotas['aves'])
            print(f"perros:{perros}" )
            print(f"gatos: {gatos}" )
            print(f"aves: {aves}")
            total=perros+gatos+aves
            print(f"el total es {total}")
