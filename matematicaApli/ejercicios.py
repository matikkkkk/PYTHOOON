# num=int(input("ingrese un numero: "))
# if num>0:
#     print("el mumero es positivo")
# elif num<0:
#     print("el numero es negativo")
# else:
#     print("el numero es 0")

# num=int(input("ingrese un numero: "))
# if num %2==0:
#     print("el numero que ingresaste  es par")
# else:
#     print("el numero que ingresaste es impar")



# Escribe un código que, mediante un ciclo *while*, sume los primeros $100 números naturales.
# suma=0
# contador=1
# while contador<=100:
#     suma+=contador
#     contador+=1
# print(suma)


# contrasena="contrasena"
# password=input("ingese contrasena: ")
# while password!=contrasena:
#     password=input("ingese contrasena: ")
# print("Contrasena correcta!!") 

# num=int(input("ingrese un numero"))
# for i in range(12):
#     print(f"{num} x {i+1} = {num*(i+1)}")

# def func1(n,m):
#     return n*m

# def func2(produc):
#     return round(produc)

# def func3():
#     num1=float(input("ingrese un numero"))
#     num2=float(input("ingrese un segundo numero"))
#     produc=num1*num2
#     redondeo=func2(produc)

# def cambiogrados(celcius):
#     farenheit=(9/5)*celcius+32
#     return farenheit
# def calculo():
#     grados=int(input("ingrese los grados celcius que desea cambiar: "))
#     farenheit=cambiogrados(grados)
#     print(f"los {grados} celcius a farenheit son {farenheit}")
# calculo() 

# import random
# numeros=[]
# for i in range(10):
#     numerosrandoms=random.randint(1,100)
#     numeros.append(numerosrandoms)
# print(numeros)
# print(numeros[1])
# print(numeros[5])

# def imcc():
#     peso=int(input("ingrese peso del paciente en kg: "))
#     altura=float(input("ingrese cuanto mide: "))
#     altura*=altura
#     imc=peso/altura
#     imc=round(imc,2)
#     print(imc)
#     if imc<18.5:
#         print("Bajo peso")
#     elif imc>=18.5 and imc<=24.9:
#         print("peso normal")
#     elif imc>=25 and imc<=29.9:
#         print("sobrepeso")
#     elif imc>=30:
#         print("obesidad ")
# imcc()

# imc=[16.43,19.31,10.25,18.63,17.85,19.76,23.64,21.94,21.3,22.67,16.48]
# print(f"la lista imc de algunos pacientes es : {imc}")
# bajo=[]
# for i, v in enumerate(imc):
#     if v<18.5:
#         bajo.append((i, v))
# for i, v in bajo:
#     print(f"indice {i},  y su imc de bajo peso es de: {v}")

    
