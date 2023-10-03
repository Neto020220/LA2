# 1.- convertir la lista en un set para eliminar duplicados
# 2.- Cacular la suma de los numeros usando una lista 
# 3.- Calcular la suma de los numeros usando un set 
# 4.- Crear un diccionario para almacenar las estadisticas 
#     numeros unicos, suma total lista, suma total set
#     maximo valor, minimo valor 
#4.- imprimir las estadisticas          


# 1.- convertir la lista en un set para eliminar duplicados
# lista 
numeros1 = [1,2,3,4,5,6,7,8,5,7,1]
# lista convertida a set´para eliminar duplicados 
numerosSet1 = set(numeros1)
#print(numerosSet1)

# 2.- Cacular la suma de los numeros usando una lista 
sumaLista1 = sum(numeros1)
#print(sumaLista1)

# 3.- Calcular la suma de los numeros usando un set 
sumaSet1 = sum(numerosSet1)

# 4.- Crear un diccionario para almacenar las estadisticas 
#     numeros unicos, suma total lista, suma total set
#     maximo valor, minimo valor 

a = max(numeros1)
b = min(numeros1)

diccionario = {
    "numeros unicos:": numerosSet1,
    "suma total lista": sumaLista1,
    "suma total set": sumaSet1,
    "Maximo valor":a,
    "Minimo valor":b


}
print(diccionario)

