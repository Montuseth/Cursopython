class MiClase:
    
    variable = "Variable clase"
    
    def __init__(self):
       self.variable_instancia = "variable instancia"
    
    @staticmethod
    def metodo_estatico():
        print("Metodo estatico")
        print(MiClase.variable)
        #print(MiClase.variable_instancia)
        
    @classmethod
    def metodo_clase(cls):
        print("metodo de clase: ", str(cls), cls.variable)

    def metodo_instancia(self):
        print(self.variable_instancia)


objeto1 = MiClase()
objeto1.metodo_instancia()
MiClase.metodo_estatico()
MiClase.metodo_clase()