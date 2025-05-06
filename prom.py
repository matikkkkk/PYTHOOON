puntajeB=0
cantramos=int(input("cuantos ramos tienes"))
for i in range(cantramos):
    notas=int(input("ingrese la nota numero", i+1))
    notas+=notas
prom=notas/cantramos
if prom>=4.0 and 5.0:
    print    