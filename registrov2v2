print("Bienvenido...")
usuario1= None
usuario2=None
usuario3=None
contrasena1= None
contrasena2=None
contrasena3= None
import time
def iniciar():
    global usuario1, usuario2, usuario3, contrasena1, contrasena2, contrasena3
    if usuario1 is None and usuario2 is None and usuario3 is None:
        print("debe registrarse primero")
    else:
        op=int(input('''con que usuario desea iniciar sesion?
                        1.- usuario 1
                        2.- usuario 2
                        3.- usuario 3'''))
        while True:
            match op:
                case 1:
                    if usuario1 is None and contrasena1 is None:
                        print("aun no se ha registrado con este usuario")
                        break
                    else:   
                        usuario=(input("ingrese usuario"))
                        contrasena=(input("ingrese contrasena"))
                        if usuario==usuario1 and contrasena==contrasena1:
                            print("inicio de sesion exitoso...")
                            time.sleep(1)
                            menusecundario()
                            break
                        else:
                            print("usuario o contrasena incorrectos")
                            break
                case 2:
                    if usuario2 is None and contrasena2 is None:
                        print("aun no se ha registrado con este usuario")
                        break
                    else:
                        usuario=(input("ingrese usuario"))
                        contrasena=(input("ingrese contrasena"))
                        if usuario==usuario2 and contrasena==contrasena2:
                            print("inicio de sesion exitoso...")
                            time.sleep(1)
                            menusecundario()
                            break
                        else:
                            print("usuario o contrasena incorrectos")
                            break

                case 3:
                    if usuario3 is None and contrasena3 is None:
                        print("aun no se ha registrado con este usuario")
                        break
                    else: 
                        usuario=(input("ingrese usuario"))
                        contrasena=(input("ingrese contrasena"))
                        if usuario==usuario3 and contrasena==contrasena3:
                            print("inicio de sesion exitoso...")
                            time.sleep(1)
                            menusecundario() 
                            break
                        else:
                            print("usuario o contrasena incorrectos")
                            break

                case _: 
                    print("elija una opcion correcta")                   
def registro():
    global usuario1, usuario2, usuario3, contrasena1, contrasena2, contrasena3
    while True:
        opc=int(input('''elija con que usuario desea entrar 1, 2 o 3 '''))
        match opc:
            case 1:
                if usuario1 is None and contrasena1 is None:
                    usuario=input("ingrese su usuario")
                    contrasena=input("ingrese contrasena")
                    usuario1=usuario
                    contrasena1=contrasena
                    print("usuario registrado con exito")
                    break
                else:
                    print("usuario ya registrado anteriormente")
                    break    
            case 2:
                if usuario2 is None and contrasena2 is None:
                    usuario=input("ingrese su usuario")
                    contrasena=input("ingrese contrasena")
                    usuario2=usuario
                    contrasena2=contrasena
                    print("usuario registrado con exito")
                    break 
                else:
                    print("usuario ya registrado anteriormente")
                    break 
            case 3:
                if usuario3 is None and contrasena3 is None:
                    usuario=input("ingrese su usuario")
                    contrasena=input("ingrese contrasena")
                    usuario3=usuario
                    contrasena3=contrasena
                    print("usuario registrado con exito")
                    break 
                else:
                    print("usuario ya registrado anteriormente")
                    break 
def realizarllamada():
    while True:
        numero = input("Ingrese número de celular ej: 912345678: ")
        if numero[0] == "9":
            print(f"Llamando al número {numero}")
            break
        else:
            print("Número inválido. Debe comenzar con 9")
def enviarcorreo():

    while True:
        correo = input("Ingrese correo electrónico: ")
        if "@" in correo:
            break
        else:
            print("Correo inválido. Debe contener '@'.")
    
    mensaje = input("Ingrese el mensaje a enviar: ")
    print(f"Correo enviado a: {correo}")
    print(f"Mensaje: {mensaje}")
def menusecundario():
    while True:
        print("menú de usuario ")
        print("1) Realizar llamada")
        print("2) Enviar correo electrónico")
        print("3) Cerrar sesión")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                realizarllamada()
            elif opcion == 2:
                enviarcorreo()
            elif opcion == 3:
                print("Sesión cerrada")
                break
            else:
                print("Opción no válida. Intente nuevamente")
        except Exception as error:
            print(f"Error: {error}. Intente nuevamente")  
def menu():
    while True:
        try:
            op=int(input('''1) iniciar sesión
                            2) registrar usuario
                            3) salir'''))
            match op:
                case 1:
                    iniciar()
                case 2:
                    registro()
                case 3:
                    print("cerrando sesion")
                    break
                case _:
                    print("opcion no valida intente denuevo")
        except ValueError as error:
            print(f"intente denuevo error:{error} ")           
menu()                   