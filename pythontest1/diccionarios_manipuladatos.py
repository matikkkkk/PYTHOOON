#el codigo debe tener 2 mayus 2minusculas y 4 numeros
def mostrar(dic):
      for a, d in dic.items():
                print(a, d)
def validacod(cod):
    mayus=0
    minus=0
    numero=0
    for palabra in cod:
        if palabra.isupper():
            mayus+=1
        if palabra.islower():
            minus+=1
        if palabra.isdigit():
            numero+=1   
    if mayus >= 2 and minus >= 2 and numero >= 4:
        return True 
    else:
         return False
def borrar(borrar):
     mostrar(juegos)
     elimi=int(input("ingrese el juego que desea borrar"))
     del juegos [elimi]
      
juegos={
    1:{
        "nombre": "Metroid Dread",
        "precio": 50000,
        "code": "MMdd23"


     }
}
while True:
    opcion=int(input("""que desea hacer?
                     1.- añadir
                     2.- mostrar 
                     3.- actualizar
                     4.- borrar
                     """))
    match opcion:
        case 1:
            nom=input("ingrese un nombre de un juego")
            prec=int(input("ingrese un precio"))
            code=input("ingrese codigo")
            if validacod(code) == False:
                print("codigo invalido, debe tener 2 mayusculas, 2 minusculas y 4 numeros")
                continue
            largo=len(juegos)
            juegos[largo + 1] = {
        "nombre": nom,
        "precio": prec,
        "code": code
     }      
        case 2:
             mostrar(juegos)
        case 3:
                mostrar(juegos)
                num=int(input("Ingrese el num del juego que desea actualizar"))
                print(juegos[num])
                actuali=(int(input("que desea actualizar: 1.- nombre, 2.- precio, 3.- codigo")))
                match actuali:
                    case 1:
                        nom=input("ingrese un nombre de un juego")
                        juegos[num]["nombre"] = nom
                    case 2:
                        prec=int(input("ingrese un precio"))
                        juegos[num]["precio"] = prec
                    case 3:
                        code=input("ingrese codigo")
                        juegos[num]["code"] = code
        case 4: 
              borrar(juegos)
        case 5: 
              print("saliendo")
              break  
        case _:
              print("ingrese opcion valida")    

