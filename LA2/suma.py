#----------------------------------
#30/08/23
#----------------------------------
# texto = "Son las 7 de la noche"

# for letra in texto:
#     if letra == "7":
#         numero = int(letra)

#         if numero < 8:
#             print("Es hora de irnos, son las 7")


#---------------------------------
#31/08/23
#---------------------------------
# Slincing String 

b = "Hola Mundo"
#c = b[5:9]

#print(c)

# Slice desde el inicio 
print(b[:5])

#Slice desde una posicion hasta el final 
print(b[2:])

#Slice con posiciones negativas 
print (b[-5:-2])

#Boleanos
#mayor que 
print(10>9)
#igual que 
print(5==5)
#menor que 
print(10<9)

#variables boleanas 
enStock = True
isTiendaAbierta = True

if enStock and isTiendaAbierta:
    print("vender productos")


tieneEfectivo = True
tieneTarjeta = True 

if tieneTarjeta or tieneTarjeta:
    print("vender productos")

if tieneTarjeta or tieneTarjeta:
    print("pago aceptado")    


regresasteConEx = False

if not regresasteConEx:
    print ("mentiroso")

tienesNovia = False

if not tienesNovia:
    print("falso")


paseLenguajes = True

if not paseLenguajes:
    print ("reprobaste")


isUploaded = True 

if not isUploaded: 
    print("reintentar")