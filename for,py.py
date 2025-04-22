# uso de for

# num=int(input())
# for i in range(10):
#     print(num, "x", i+1, "es",  (i+1)*num)

cant=int(input("ingrese el num de notas "))
suma=0
for i in range(cant):
    print("ingrese la nota", i+1)
    nota=float(input())
    suma=suma+nota

prom=suma/cant
print("su promedio de notas es", round(prom, 1))
 
if prom>=4:
  print("aprovado")
else:
  print("no pasó")