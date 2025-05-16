cantalumno=int(input("que cantidad de alumnos son"))
for i in range(cantalumno):
    print("alumno numero", 1+i)
    cantnotas=int(input("cuantas notas tienes?: "))
    for j in range(cantnotas):
        sumanotas=0
        notas=float(input(f"ingrese la nota numero   {j+1} "))
        sumanotas+=notas
        prom=sumanotas/cantnotas
    print("el promedio del alumno: ", i+1, "es :", prom)

