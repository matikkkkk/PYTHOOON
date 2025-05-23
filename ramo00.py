
decimas=0
talleres=4
Tasistidos=0
cantrojos=int(input("Cuantos ramos rojos hay en el curso:  "))
for i in range(1, talleres + 1):
    resp=int(input(f'''usted asistio al taller nro {i}
                    1.- si 
                    2.- no
'''))    
    if resp==1:
        Tasistidos+=1
decimas=Tasistidos*0.3

if cantrojos<=1:
    print("usted tiene la bendicion del profesor")
    print("tienes esta cantidad de decimas: ", decimas)
    notafi=float(input("ingrese su nota final: "))
    notafi+=decimas
    print("su nota final con decimas es: ", round(notafi, 2))
    if notafi>=4.0:
        print("Usted aprobo")
    else:
        print("usted reprobo")
else:
    print("no se le puede ayudar tiene demasiados rojos")




    