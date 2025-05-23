
# En un delivery de Sushi vende 4 tipos de Sushi:
# 1. Pikachu Roll $4500
# 2. Otaku Roll $5000
# 3. Pulpo Venenoso Roll $5200
# 4. Anguila Eléctrica Roll $4800
# La empresa le ha solicitado a usted, que genere una pequeña aplicación en Python para tomar el pedido de un
# cliente el cuál puede ir agregando Rolls a través de un menú uno por uno con solo seleccionar la opción (1 a 4)
# La aplicación debe mostrar en un menú los Rolls que agregará el usuario, esto se debe repetir hasta que el usuario
# decida que su pedido está completo.
# Luego de ello, debe preguntar al usuario si posee un código de descuento. En caso de que posea el código, deberá
# ingresarlo. Si el código ingresado es “soyotaku”, debe realizar un 10% de descuento al total del pedido, en caso
# contrario enviar el mensaje “código no válido” y dar al usuario la opción de reingresar el código o volver al menú
# tecleando “X”
# Una vez realizado los pasos anteriores, debe mostrar el detalle del pedido contabilizando el total de productos y la
# cantidad de cada uno de ellos y si aplica o no el descuento
# ******************************
# TOTAL PRODUCTOS:4
# ******************************

def bole():
    print("INGRESANDO AL CARRITO...")     
    print(f'''*****************************
        TOTAL PRODUCTOS:{productostotal}
        ***************************** ''')
    print(f"precio total de los productos...: {total} ")
import time
def t():
    time.sleep(1)
productostotal=0
precio=0
total=0
codigo=""
print("ingresando al delivery...")
t()

while True:
    accion=int(input('''que quiere hacer
                1.- Comprar
                2.- Ver carrito
                '''))
    match accion:
        case 1:
            while True:
                opc=int(input('''Delivery de sushi vende 4 tipos de sushi:
                            1.- Pikachu roll $4500
                            2.- Otaku roll $5000
                            3.- Pulpo Venenoso Roll $5200
                            4. Anguila Eléctrica Roll $4800
                            5.- salir al menu
                            '''))
                match opc:
                    case 1:
                        print("usted lleva picachu rolls $4500 ")
                        precio+=4500
                        productostotal+=1
                    case 2: 
                        print("usted lleva Otaku Roll $5000")
                        precio+=5000
                        productostotal+=1
                    case 3:
                        print("usted lleva Pulpo Venenoso Roll $5200")
                        precio+=5200 
                        productostotal+=1
                    case 4:
                        print(" usted lleva Anguila Eléctrica Roll $4800")
                        precio+=5000
                        productostotal+=1
                    case 5: 
                        print("volviendo al menu")
                        break    
        case 2:
                while codigo!="soy gay":
                    cod=input("¿Tiene código de descuento? 1.- Sí 2.- No: ")
                    if cod == "1":
                        codigo = input("Ingrese su código de descuento: ")
                    if codigo =="soygay":
                       print("Descuento aplicado de 10%.")
                       descuento = precio * 0.1  
                       total = precio - descuento  
                       bole()
                       break
                    else:
                        print("codigo no valido")
                        nu=input("desea intentar nuevamente?. 1.- si 2.- no")
                        if nu!="1":
                            total=precio
                            bole()
                            break
                break
 
    

                          

                                      
                                    
                                               




                                
                    


        






        
        


