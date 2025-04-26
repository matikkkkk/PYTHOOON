# #EXPLICACION DE WHILE
# import time
# num=10
# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

#resp="no"
#while resp!="si":
    #resp=input("desea salir del sistema?")

#clave=2233
#contraseña=int(input("ingrese su contraseña "))
#while clave!=contraseña:
#    contraseña=int(input("ingrese su contraseña"))
#print("clave correcta")

clave=2255
intento=1
limite=10

contrasena=int(input("ingrese su coontrasena "))
print("intento nro", intento)

while  contrasena!= clave and intento<limite:
    print("error")
    intento=intento+1
    contrasena=int(input("ingrese su coontrasena "))
    print("intento nro", intento)
    
if contrasena == clave:
    print("Contraseña correcta")
else:
    print("muchos intentos...")



