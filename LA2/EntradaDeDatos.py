#Entrada de datos: 
print ("ingresa tu numbre")
nombre = input()
print(type(nombre))

palabras = nombre.split(" ")

nombre = nombre.capitalize()
#nombre = nombre.replace(" ","-")



capitalizado = [p.capitalize() for p in nombre.split()]
concatenar = ' '.join(capitalizado)

print(concatenar)
#print(palabra.capitalize())

#print("Tu nombre es " + nombre)