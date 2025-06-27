estudiantes={}

while True:
    opc=int(input("""
    1.- Ingresar 
    2.- Mostrar 
    3.- Actualizar
    4.- Borrar 
    6.- Salir"""))
    match opc:
        case 1:
            nom=input("ingresa nombre del estudiante")
            edad=int(input("ingresa edad"))
            curso=(input("ingresa curso"))
            prome=float(input("ingresa promedio"))
            if estudiantes:
                largo=max(estudiantes.keys())+1
            else:
                largo=1
            estudiantes[largo]={
            "nombre": nom,
            "edad" : edad,
            "curso" : curso,
            "promedio" : prome
            }
        case 2:
            for k, v in estudiantes.items():
                print(k, v)
        case 3:
            while True:
                for k, v in estudiantes.items():
                    print(k, v)
                try:
                    act=int(input("ingresa el numero del estudiante a actualizar"))
                    if act in estudiantes:
                        nom=input("ingresa nombre del estudiante")
                        edad=int(input("ingresa edad"))
                        curso=(input("ingresa curso"))
                        prome=float(input("ingresa promedio"))
                        estudiantes[act]={
                            "nombre": nom,
                            "edad" : edad,
                            "curso" : curso,
                            "promedio" : prome
                        }
                    else:
                        print("numero de estudiante no encontrado")
                except Exception as e:
                    print(f"Error: {e}")
                    continue

        case 4:
            while True:
                for k, v in estudiantes.items():
                    print(k, v)
                try:
                    borr=int(input("ingresa el numero del estudiante a borrar"))
                    if borr in estudiantes:
                        del estudiantes[borr]
                        print("Estudiante borrado")
                    else:
                        print("numero de estudiante no encontrado")
                except Exception as e:
                    print(f"Error: {e}")
                continue
        case 6:
            print("Saliendo del programa") 
            break