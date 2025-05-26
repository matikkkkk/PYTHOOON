
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
#Subtotal por pagar: 
#Descuento por código: 
#TOTAL: )   
otakur=0
picar=0
productostotal=0
precio=0
pulpove=0
angui=0
desc=0
total=0
while True:
    opd=int(input('''ingresando a delivery de sushiblues
                 1.- comprar
                 2.- ver carrito
                 3.- pagar        
              '''))
    match opd:
        case 1:
           while True:
                opc=int(input('''Delivery de sushi vende 4 tipos de sushi:
                                    1.- Pikachu roll $4500
                                    2.- Otaku roll $5000
                                    3.- Pulpo Venenoso Roll $5200
                                    4. Anguila Eléctrica Roll $4800
                                    5.- salir al menu'''))
                match opc:
                        case 1:
                                print("usted lleva picachu rolls $4500 ")
                                precio+=4500
                                productostotal+=1
                                picar+=1
                        case 2: 
                                print("usted lleva Otaku Roll $5000")
                                precio+=5000
                                productostotal+=1
                                otakur+=1
                        case 3:
                                print("usted lleva Pulpo Venenoso Roll $5200")
                                precio+=5200 
                                productostotal+=1
                                pulpove+=1
                        case 4:
                                print(" usted lleva Anguila Eléctrica Roll $4800")
                                precio+=4800
                                productostotal+=1
                                angui+=1
                        case 5: 
                                print("volviendo al menu")
                                break
        case 2:
                print(f'''      ******************************
                                TOTAL PRODUCTOS:{productostotal}
                                ******************************
                                Pikachu Roll : {picar}
                                Otaku Roll : {otakur}
                                Pulpo Venenoso Roll: {pulpove}
                                Anguila Eléctrica Roll:{angui}
                                ****************************** 
                        ''')

                op=int(input("Presione 0 para volver al menu"))
                if op==0:
                    continue
        case 3:
            cod=int(input("usted tiene codigo de desc?: 1.- si 2.- no")) 
            if cod==1:
                  while True:
                        codigo=input("ingrese codigo de desc/ para salir aprete s ")
                        if codigo=="soygay":
                            print("codigo de desc aplicado de 10%")
                            desc=precio*0.1
                            total=precio-desc
                            print(f'''  ******************************
                                        TOTAL PRODUCTOS:{productostotal}
                                        ******************************
                                        Pikachu Roll : {picar}
                                        Otaku Roll : {otakur}
                                        Pulpo Venenoso Roll: {pulpove}
                                        Anguila Eléctrica Roll:{angui}
                                        ****************************** 
                                        Subtotal por pagar: {precio}
                                        Descuento por código:{desc} 
                                        TOTAL: {total}   
                                            ''')
                            break
                        elif codigo=="s":
                            print("no se aplico ningun desc")
                            total=precio
                            desc=0
                            print(f'''TOTAL PRODUCTOS:{productostotal}
                            ******************************
                            Pikachu Roll : {picar}
                            Otaku Roll : {otakur}
                             Pulpo Venenoso Roll: {pulpove}
                            Anguila Eléctrica Roll:{angui}
                            ****************************** 
                            Subtotal por pagar: {precio}
                            Descuento por código:{desc} 
                            TOTAL: {total}''')
                            break
                        else:
                            print("cod invalido, intente nuevamente si quiere salir aprete s")
            else:
                  desc=0
                  total=precio
                  print(f'''******************************
                            TOTAL PRODUCTOS:{productostotal}
                            ******************************
                            Pikachu Roll : {picar}
                            Otaku Roll : {otakur}
                             Pulpo Venenoso Roll: {pulpove}
                            Anguila Eléctrica Roll:{angui}
                            ****************************** 
                            Subtotal por pagar: {precio}
                            Descuento por código:{desc} 
                            TOTAL: {total}
                                        ''')
                  break
                               
                
                              
                              
                              
                              

                            

                              

                
              

                          

                                      
                                    
                                               




                                
                    


        






        
        


