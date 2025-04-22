# sacar promedio de 3 numeros

print("ingrese 3 notas")

n1=float(input())
n2=float(input())
n3=float(input())
prom=(n1+n2+n3)/3
print("el promedio de", n1, n2, n3 ,"es", round(prom, 2))

if prom>=40:
    print("el estudiante aprobó")
else:
    print("el estudiante reprobó")
    