class Rectangulo:
    def __init__(self,altura,base):
        self.altura = altura
        self.base = base
    
    def area(self):
        return self.altura * self.base

alturaU = int(input("Ingrese Altura: "))
baseU = int(input("Ingrese base: "))
rect = Rectangulo(alturaU,baseU)
print(rect.area())