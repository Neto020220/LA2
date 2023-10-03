# condiciones 
a = 280
b = 33

if b > a:
    print("b es maroy que a")
elif a == b: 
    print("a y b son iguales")
else:
    print("a es mayor que b")        


# ciclo while
quiereVolver = True
vecesRegresaron = 0
while vecesRegresaron <= 3:
    print(f"Han vuelto {vecesRegresaron} veces")
    vecesRegresaron += 1



i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1     


# continue 
i = 0
while i < 6: 
    i += 1
    if i == 3:
        continue
    print(i)

else: 
    print("error")




# Ciclo For

frutas = ["🍎","🍌","🥭"]

for fruta in frutas:
    if fruta == "🍌":
        print("Se encontro " + fruta)

    else: 
        print("No coincide")    
    #print(fruta)


else: 
    print("No se esta buscando")    



"""

"""

