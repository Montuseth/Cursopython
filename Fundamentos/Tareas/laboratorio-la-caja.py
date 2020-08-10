class Caja:
    def __init__(self, alto, ancho,largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
    
    
    def volumen(self):
        return self.ancho * self.largo * self.alto
    
anchou = int(input("ingrese ancho: "))
altou = int(input("ingrese alto: "))
largou = int(input("ingrese largo: "))

caja = Caja(altou,anchou,largou)
print(caja.volumen())