# Clases y objetos 
# Creando la clase
class alumno:
    def __init__(self, nombre):
        self.nombre = nombre

    #nombre = "Neto"


# Creando el objeto
alumnoChem = alumno("Chencho")    
alumnoChes = alumno("Chester")    
alumnoToño = alumno("Toño")    

print(alumnoChem.nombre)
print(alumnoChes.nombre)
print(alumnoToño.nombre)