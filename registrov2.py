print("Bienvenido...")
usuario1= None
usuario2=None
usuario3=None
contrasena1= None
contrasena2=None
contrasena3= None
def registro():
    global usuario1, usuario2, usuario3, contrasena1, contrasena2, contrasena3
    print("REGISTRO.")
    while True:
        nuevousu=input("ingrese nuevo usuario")
        nuevacontr=input("ingrese nueva contrasena")
        if usuario1==None:
            usuario1=nuevousu
            contrasena1=nuevacontr
            break
        elif usuario2==None:
            usuario2=nuevousu
            contrasena2=nuevacontr
            break
        elif usuario3==None:
            usuario3=nuevousu
            contrasena3=nuevacontr
            break
        else:
            print("no se pueden agregar mas usuarios")
            break
def iniciar():
    while True:
        if usuario1==None and usuario2==None and usuario3==None:
            print("debe  ingresar al menos un usuario para iniciar sesion")
            break
        else:
            usuario=input("ingrese usauri")
            contrasena=input("ingrese contrasena")
            if usuario==usuario1 and contrasena==contrasena1:
                 print("inicio de sesion exitoso")
                 menu_secundario()
                 break
            elif(usuario == usuario2 and contrasena == contrasena2):
                  print("inicio de sesion exitoso")
                  menu_secundario()
                  break
                  
            elif(usuario == usuario3 and contrasena == contrasena3):
                 print("inicio de sesion exitoso")
                 menu_secundario()
                 break
            else:
                print("Usuario o contraseña incorrectos")
                break     






def realizarllamada():
    while True:
        numero = input("Ingrese número de celular ej: 912345678: ")
        if numero[0] == "9":
            print(f"Llamando al número {numero}...\n")
            break
        else:
            print("Número inválido. Debe comenzar con 9 y tener 9 dígitos")
            

def enviarcorreo():
    while True:
        correo = input("Ingrese correo electrónico: ")
        if '@' in correo:
            break
        else:
            print("Correo inválido. Debe contener '@'.\n")
    
    mensaje = input("Ingrese el mensaje a enviar: ")
    print(f"\nCorreo enviado a: {correo}")
    print(f"Mensaje: {mensaje}\n")

def menu_secundario():
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
        except Exception as error:
            print(f"intente denuevo error:{error} ")           
menu()