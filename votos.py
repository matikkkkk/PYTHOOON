goku=0
vegeta=0
broly=0
cant=int(input("ingreses cantidad de votantes  "))

for i in range (cant):
    print('''  
           1.- goku 
            2.- vegeta
            3.- broly
      ''')
    op=int(input())
    if op==1:
        print("usted votó por goku")
        goku=goku+1
    elif op==2:
        print("usted votó por vegeta")
        vegeta=vegeta+1
    elif op==3:
        print("usted  votó por broly")
        broly=broly+1
    else:
        print("voto invalido")

    
print("los votos de goku son", goku)
print("los votos de vegeta son", vegeta)
print("los votos de broly son", broly)

if goku>vegeta and goku>broly:
    print("ganó goku con", goku,"votos")
elif vegeta>broly and vegeta>goku:
    print("ganó vegeta con", vegeta, "votos")
elif broly>vegeta and broly>goku:
    print("ganó broly", broly, "votos")
else:
    print("empataron")
    