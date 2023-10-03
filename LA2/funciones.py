# Funciones

x = 2

def saludar(nombre, edad):
    print(f"Hola {nombre} edad {edad}")
    

if x == 1:

    saludar("Chencho",21)

if x == 2:
    saludar("Chester",21)

if x == 3:    
    saludar("Toño",22)


# Multiparametros 
def asistencia(*alumnos):

    for alumno in alumnos: 
        print(f"asistio: {alumno}")
    
asistencia("CHENCHO", "TOÑO", "CHESTER")       


#