class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "Color: " + self.color + " ruedas: " + str(self.ruedas)    

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return super().__str__() + " velocidad(km/hr) = " + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + " tipo: " + str(self.tipo)


vehi = Vehiculo("Rojo",19.9)
print(vehi.__str__());

coche = Coche("Azul",20.1,130)
print(coche.__str__())

bici = Bicicleta("amarilla",12,15)
print(bici.__str__())
