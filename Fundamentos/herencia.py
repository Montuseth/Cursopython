class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def __str__(self):
            return "nombre:" + self.nombre + " edad: "+ str(self.edad)
        
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return super().__str__() +" sueldo:     "+ str(self.sueldo)
persona = Persona("JUAN",28)
print(persona)

empleado = Empleado("Juan",18,2323.33)
print(empleado)