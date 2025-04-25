palabra=input("ingrese una frase ")
cont=0
vocales=0
cons=0

for i in palabra.lower():
    cont=cont+1  
    print(cont, i )
    if i in "aeiou":
        vocales+=1
    else:
        cons+=1

print("la cantidad de caracteres son", cont)
print("la cantidad de vocales son", vocales)
print("la cantidad de cons son", cons)  