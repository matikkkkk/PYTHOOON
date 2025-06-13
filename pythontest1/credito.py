credito=0
caningre=int(input(('''En que rango esta su cantidad de ingreso?
                    1.- 500.000 - 1.000.000
                    2.' 1.000.001 - 1.500.000
                    3.- 1.500.001 o mas''')))
match caningre:
    case 1:
        print("su credito equivale a 300.000")
        credito+=300000
    case 2: 
        print("su credito equivale en 650.000") 
        credito+=650000
    case 3:
        print("su credito equivale en 1.000.000")
        credito+=1000000
niveledu=int(input('''que nivel educaciional tiene?
                    1.- Basico(1x)
                    2.- medio(1.3x)
                    3.- superior(1.5x)
                   '''))
match niveledu:
    case 1: 
        print("su credito aumentó en 1x")
        credito*1
    case 2:
         print("su credito aumentó en 1.3x")
         credito*=1.3
    case 3:
         print("su credito aumentó en 1.5x")
         credito*=1.5
nacional=int(input('''Que nacionalidad es:
                      1.- CHILENA
                      2.- EXTRANJERO'''))         
match nacional:
    case 1:
        print("usted es chileno y aumentó en 300.000")
        credito+=300000     
    case 2: 
        print("usted es extrannjero y su credito aumentó en 0")
        credito+=0
print("Su credito final es de", credito)



        

