notas=[]
promedio=0
suma=0
import time
while True:
    try:
        op=(int(input("""
            1.- INGRESAR NOTA
            2.- BORRAR NOTA
            3.- MOSTRAR NOTAS 
            4.-SACAR PROMEDIO, NOTA MAYOR Y NOTA MENOR
            5.- LIMPIAR TODAS LAS NOTAS
            6.- SALIR """)))
        match op:
            case 1:
                no=float(input("ingrese nota"))
                notas.append(no)
            case 2:
                for i in range(len(notas)):
                    print(f"{i+1}.-{notas[i]} ")
                deletenot=int(input("que nota desea eliminar"))-1
                notas.pop(deletenot)    
            case 3:
                for i in range(len(notas)):
                    print(f"{i+1}.-{notas[i]} ")
            case 4:
                for i in range(len(notas)):
                    print(f"{i+1}.-{notas[i]} ")
                    suma+=notas[i]
                promedio=suma/len(notas)
                print(f"el promedio de las notas es {promedio}")
                notas.sort()
                print(f"la nota mayor de la lista es,{notas[-1]} ")
                print(f"la nota menor es {notas[0]}")
            case 5:
                print("LIMPIANDO NOTAS...")
                time.sleep(1)
                notas=[]
            case 6:
                print("saliendo...")
                break
            case _:
                print("opcion invalida")
    except Exception as e:
        print(f"ERROR. {e}")                   



        
