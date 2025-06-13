# nombre y mayor de edad o no
print("ingrese su nombre")
nombre=input()
print("ingresa tu edad")
edad=int(input())

if edad<12:
    print("tu nombre es", nombre, "y eres un niño")
elif edad>=12 and edad<18:
    print("tu nombre es", nombre, "y eres adolencente")
elif edad>=18 and edad<=64:
    print("tu nombre es", nombre, "y es adulto ")
else: 
    print("tu nombre es", nombre, "y es mayor de edad ")

