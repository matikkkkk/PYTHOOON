
num2=0
import random

num1=int(input(("elija un numero: ")))
while num1>=num2:
    print("el segundo numero tiene que ser mayor que el anterior")
    num2=int((input("elija su numero n2 : ")))
numran=random.randint(num1, num2)
print("el numero generado entre ", num1, "y", num2, "es ",numran )
for i in range (numran):
    print("▄"*numran)