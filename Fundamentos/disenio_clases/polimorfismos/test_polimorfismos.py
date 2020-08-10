from empleado import Empleado
from gerente import Gerente

def imprime_tipo_padre(tipo_padre):
    print(tipo_padre)
    print(type(tipo_padre),end="\n\n") 
    if isinstance(tipo_padre,Gerente):
         print(tipo_padre.departamento)

e = Empleado("Juan", 5000)
imprime_tipo_padre(e)
e = Gerente("Rodrigo",300,"Prod")
imprime_tipo_padre(e)