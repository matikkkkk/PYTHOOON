estudiantes={

}

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
            for k, v in estudiantes.items():
                print(k, v)

    # 1: {
    #         "nombre": "ricardo",
    #         "edad" : 18,
    #         "curso" : "cuarto medio",
    #         "promedio": 6.3 
    #         }