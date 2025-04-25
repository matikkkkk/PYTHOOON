# #EXPLICACION DE WHILE
# import time
# num=10
# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

# resp="no"
# while resp!="si":

#     resp=input("desea salir del sistema?")

clave=2233
contraseña=int(input("ingrese su contraseña "))
while clave!=contraseña:
    print("error clave invalida")
    contraseña=int(input("ingrese su contraseña"))
print("clave correcta")



               