# Preguntar al usuario cuantos productos llevará
# 	 escribir listado de 3 productos y sus precios
# 	mostrar el total neto de la compra
# 	 y mostrar el total mas IVA (19%)
total=0

cant=int(input("cuantos productos llevará? "))
for i in range (cant):
     print('''
		1.- Diazepam $9000
		2.- Metametozona $18500
		3.- Oblea China $1000''')
     op=int(input())
     if op==1:
          print("usted lleva diazepam")
          total=total+9000
     elif op==2:
          print("usted lleva metametazona")
          total=total+18500
     elif op==3: 
           print("usted lleva metametazona")
           total=total+100
     else:
      print("opcion no valida")
print("EL total neto es ", total)
print("EL total neto es ", total*1.19)    



     


          
           
    
          
        
          
        
        
