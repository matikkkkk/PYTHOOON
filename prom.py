puntajeB=0
sumaprom=0
cantramos=int(input("cuantos ramos tienes: "))
print("tienes ", cantramos, "ramos")
for i in range(cantramos):
    print("ramo numero", 1+i)
    sumanotas=0
    cantnotas=int(input("cuantas notas tienes?: "))
    for j in range(cantnotas):
        notas=float(input("ingrese la nota numero "+ str(j+1)))
        sumanotas+=notas
    prom=sumanotas/cantnotas
    print("el promedio del ramo nro", i+1, "es :", prom)
    sumaprom+=prom
promto=sumaprom/cantramos
print("el promedio de todos los ramos es :", promto)

if promto>=4.0 and promto<=5.0:
    print("usted tiene +300 de beneficio ")
    puntajeB+=300
elif promto>=5.1 and promto<=6.0:
    print("usted tiene +500 de beneficio ")
    puntajeB+=500
elif promto>=6.1 and promto<=7.0:
    print("usted tiene +800 de beneficio ")
    puntajeB+=800
carrera=int(input('''
                     1. tecnico: +60
                     2. ingenieria: +40
                     3. diplomado: +20 ''')) 
match carrera:
    case 1:
        print("usted es tecnico +60")
        puntajeB+=60
    case 2:
        print("usted es ingeniero +40")
        puntajeB+=40
    case 3: 
        print("usted tiene diplomado +20")
        puntajeB+=20
print("el puntaje de beneficio total es: ", puntajeB) 
